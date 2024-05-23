# AutoNextEpisode Plugin

## Description
A Plex plugin that automatically advances to the next episode during "Watch Together" sessions and keeps playback in sync.

## Installation

1. **Download and Extract**:
   - Download the `AutoNextEpisode.bundle` directory and extract it.

2. **Copy to Plex Plugin Directory**:
   - Copy the `AutoNextEpisode.bundle` directory into the Plex plugin directory.
     - **Windows**: `%LOCALAPPDATA%\Plex Media Server\Plug-ins`
     - **macOS/Linux**: `~/Library/Application Support/Plex Media Server/Plug-ins`

3. **Configure Environment Variables**:
   - Set the following environment variables:
     ```bash
     export PLEX_URL='http://<your-plex-server-ip>:32400'
     export PLEX_TOKEN='<your-plex-token>'
     export CHECK_INTERVAL=30
     ```

4. **Restart Plex Media Server**:
   - Restart your Plex Media Server to load the new plugin.

## Usage
- Start playing an episode on Plex and let it run.
- The plugin will automatically queue the next episode as the current one approaches its end and keep all participants in sync.

## Logging
- Logs are generated to provide insights into the plugin's operations and help identify any issues.

## Development
- Ensure the `plexapi` library is installed:
  ```bash
  pip install plexapi
