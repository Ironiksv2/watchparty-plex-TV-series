# Plexwatch-for-series - Plex watch together for tv show (Help with Testing)
code - https://github.com/Ironiksv2/watchparty-plex-TV-series/tree/main/Code









## Description
The AutoNextEpisode plugin for Plex Media Server is designed to automatically advance to the next episode during "Watch Together" sessions and keep playback synchronized across all participants. This ensures a seamless viewing experience for all users, especially during binge-watching sessions.

## Installation

### 1. Download and Extract
- Download the `AutoNextEpisode.bundle` directory and extract it to a location on your computer.

### 2. Copy to Plex Plugin Directory
- Copy the entire `AutoNextEpisode.bundle` directory into the Plex plugin directory on your Plex Media Server.
  - **Windows**: `%LOCALAPPDATA%\Plex Media Server\Plug-ins`
  - **macOS/Linux**: `~/Library/Application Support/Plex Media Server/Plug-ins`

### 3. Configure Environment Variables
Set the following environment variables to configure the plugin:
```bash
export PLEX_URL='http://<your-plex-server-ip>:32400'
export PLEX_TOKEN='<your-plex-token>'
export CHECK_INTERVAL=30
```
- Replace `<your-plex-server-ip>` with the IP address of your Plex server.
- Replace `<your-plex-token>` with your Plex token. You can find your Plex token by following this guide: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

### 4. Restart Plex Media Server
- Restart your Plex Media Server to load the new plugin. This will initialize the plugin and start monitoring playback sessions.

## Usage

- Start playing an episode on Plex and let it run.
- The plugin will automatically queue the next episode as the current one approaches its end (less than 2 minutes remaining) and will synchronize playback across all participants in a "Watch Together" session.

## Logging
- Logs are generated to provide insights into the plugin's operations and help identify any issues. Logs include information about the current episode, time left, and any errors encountered during playback synchronization.

## Development
To develop the AutoNextEpisode plugin, we started with code snippets from various sources. The primary codebase came from the SyncLounge GitHub repository (https://github.com/synclounge/synclounge), which provided a foundation for synchronizing Plex playback across multiple clients. We integrated code to handle Plex's internal APIs for managing play queues and session monitoring. Throughout the process, we customized the code to meet the specific needs of advancing to the next episode during "Watch Together" sessions and ensuring playback synchronization. We also referenced Plex's internal API documentation and existing Plex plugins for guidance on structure and functionality. This collaborative effort resulted in a comprehensive plugin that enhances the user experience for group viewing sessions on Plex.


### Prerequisites
- Ensure the `plexapi` library is installed. You can install it using pip:
  ```bash
  pip install plexapi
  ```

### Directory Structure
The directory structure of the plugin should look like this:
```
AutoNextEpisode.bundle/
    Contents/
        Code/
            __init__.py
            config.py
        Info.plist
        Resources/
            icon-default.png
            fanart.jpg
    README.md
```

### Files and Their Purpose

1. **Info.plist**
   - Contains metadata about the plugin, such as its identifier, name, and version.
   - Ensures Plex recognizes the plugin and loads it correctly.

2. **config.py**
   - Manages configuration settings through environment variables.
   - Variables include `PLEX_URL`, `PLEX_TOKEN`, and `CHECK_INTERVAL`.

3. **README.md**
   - Provides detailed installation, usage, and development instructions.
   - Ensures users can set up and use the plugin effectively.

4. **\_\_init\_\_.py**
   - Contains the main logic for monitoring playback, queuing the next episode, and synchronizing playback.
   - Includes functions for handling signals, logging, and error handling.
   - The `AutoNextEpisode` class is responsible for the core functionality.

5. **Resource Files**
   - `icon-default.png` and `fanart.jpg` are optional image files used for the plugin's icon and background.

### Key Components in \_\_init\_\_.py

#### Initialization:
- Sets up the Plex server connection using the provided URL and token.
- Initializes signal handling for graceful shutdown.

#### Playback Monitoring:
- Continuously monitors active sessions to check the playback state.
- Logs the current episode and time left until the next episode should be queued.

#### Episode Queuing and Playback Synchronization:
- Identifies the next episode in the series and queues it in the play queue.
- Ensures all participants in the "Watch Together" session start the next episode simultaneously.

#### Error Handling:
- Catches and logs network errors and other exceptions to ensure the plugin runs smoothly.

## Further Improvements

### User Interface
- **Configuration Interface**: Develop a simple user interface within the Plex web app to allow users to configure the plugin settings (e.g., Plex server URL, token, check interval) without needing to set environment variables.
- **Status Dashboard**: Create a dashboard that displays the current status of the plugin, including active sessions, current episode, time left, and next episode.

### Customization Options
- **Threshold Customization**: Allow users to customize the time threshold for queuing the next episode (e.g., less than 2 minutes, less than 5 minutes).
- **Notification System**: Implement a notification system to inform users when the next episode is about to start or if there are any issues detected.

### Documentation
- **Detailed Instructions**: Update the README file to include detailed instructions on how to use the new user interface and customization options.
- **Troubleshooting Guide**: Add a troubleshooting guide to help users resolve common issues.

### Testing and Improving User Friendliness

1. **Set Up the Plugin**:
   - Ensure the `AutoNextEpisode.bundle` directory is correctly placed in your Plex plugin directory.
   - Set the required environment variables (`PLEX_URL`, `PLEX_TOKEN`, `CHECK_INTERVAL`).
   - Restart your Plex Media Server.

2. **Functionality Testing**:
   - **Playback Monitoring**: Verify that the plugin correctly monitors the playback state of the current episode.
   - **Episode Queuing**: Confirm that the next episode is queued when there are less than 2 minutes left in the current episode.
   - **Synchronization**: Ensure that playback is synchronized across all participants in a "Watch Together" session.
   - **Error Handling**: Check the logs for any errors and ensure they are handled gracefully.

3. **User Friendliness Enhancements**:
   - **User Interface**: Develop a configuration interface and status dashboard.
   - **Customization Options**: Allow users to customize the time threshold and implement a notification system.

4. **Testing the Enhancements**:
   - After implementing the enhancements, test the new features to ensure they work as expected.
   - Conduct usability testing with a few users to gather feedback on the new interface and features.

## Contributing
- Feel free to submit issues or pull requests for improvements.
- Contributions to enhance the plugin's functionality and usability are welcome.

By following these instructions and understanding the purpose of each component, you should be able to set up and use the AutoNextEpisode plugin successfully on your Plex server. If you encounter any issues, refer to the logs for debugging information and make use of the `plexapi` documentation for additional support.

## Helpful Links
- Plex API Documentation: https://python-plexapi.readthedocs.io/en/latest/
- Finding Your Plex Token: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/


 ** Thank You 

A huge thank you to everyone who contributed to the development of the AutoNextEpisode plugin. Your dedication, expertise, and collaborative spirit were essential in bringing this project to life. Special thanks to the developers and contributors from the SyncLounge. Additionally, a quick thank you to all my personal friends who contributed their time and support. This project would not have been possible without your hard work and support. Thank you for your commitment and contributions!
