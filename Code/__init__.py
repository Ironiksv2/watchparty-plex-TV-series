
### 4. `__init__.py`
```python
import time
import logging
import signal
import requests
from plexapi.server import PlexServer
from plexapi.playqueue import PlayQueue
from config import PLEX_URL, PLEX_TOKEN, CHECK_INTERVAL

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AutoNextEpisode:
    def __init__(self, server_url, token):
        self.plex = PlexServer(server_url, token)
        self.play_queues = {}
        self.sessions = {}
        self.running = True
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def shutdown(self, signum, frame):
        logger.info("Shutting down gracefully...")
        self.running = False

    def get_next_episode(self, current_episode):
        try:
            show = current_episode.show()
            episodes = show.episodes()
            for i, episode in enumerate(episodes):
                if episode == current_episode and i < len(episodes) - 1:
                    return episodes[i + 1]
        except Exception as e:
            logger.error(f'Error getting next episode: {e}')
        return None

    def sync_playback(self, next_episode):
        try:
            for s in self.sessions.values():
                client = s['client']
                client.stop()
                client.playMedia(next_episode)
        except Exception as e:
            logger.error(f'Error syncing playback: {e}')

    def monitor_playback(self):
        while self.running:
            try:
                sessions = self.plex.sessions()
                for session in sessions:
                    if session.TYPE == 'video':
                        self.sessions[session.sessionKey] = {
                            'client': session.player,
                            'state': session.state
                        }
                        current_episode = session.grandparentTitle
                        time_left = session.duration - session.viewOffset
                        logger.info(f'Current episode: {current_episode}, Time left: {time_left} ms')
                        if time_left < 120000:  # less than 2 minutes left
                            next_episode = self.get_next_episode(current_episode)
                            if next_episode:
                                logger.info(f'Next episode: {next_episode.title}')
                                # Queue the next episode
                                play_queue = self.play_queues.get(session.user.id)
                                if not play_queue:
                                    play_queue = PlayQueue.create(self.plex, [next_episode])
                                    self.play_queues[session.user.id] = play_queue
                                    logger.info('Created new play queue')
                                else:
                                    play_queue.addItem(next_episode, playNext=True)
                                    logger.info('Added next episode to existing play queue')
                                self.sync_playback(next_episode)
            except requests.exceptions.RequestException as re:
                logger.error(f'Network error: {re}')
            except Exception as e:
                logger.error(f'Error monitoring playback: {e}')
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    auto_next = AutoNextEpisode(PLEX_URL, PLEX_TOKEN)
    auto_next.monitor_playback()
