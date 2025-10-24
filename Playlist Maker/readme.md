# YouTube Playlist Manager

A simple command-line application for managing YouTube video playlists using SQLite3 database.

## Features

- Add videos with name, duration, and link
- List all videos in the playlist
- Update existing video information
- Delete videos from the playlist
- Automatic ID management after deletions

## Requirements

- Python 3.10+ (uses `match` statement)
- SQLite3 (included with Python)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application:

```bash
python main.py
```

## Usage

The application provides a menu-driven interface with the following options:

1. **List videos** - Display all videos in the database
2. **Add video** - Add new videos to the playlist
3. **Update video** - Modify existing video information
4. **Delete video** - Remove videos from the playlist
5. **Exit app** - Close the application

## Database

The application creates a SQLite database file (`youtube_videos.db`) in the same directory with the following schema:

```sql
CREATE TABLE videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL,
    link TEXT NOT NULL
)
```

## Example

When you run the application, you'll see:

```
YouTube manager app with SQLITE3
1. List videos
2. Add video
3. Update video
4. Delete video
5. Exit app
Enter your choice:
```

Simply enter the number corresponding to your desired action and follow the prompts.