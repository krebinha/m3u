# M3U Playlist Extractors

This repository contains three separate Python applications to extract and organize data from M3U playlists into a format suitable for media centers like Kodi or Plex.

## Applications

1.  **Movies Extractor**: Extracts movie entries and saves them as `.strm` files organized by movie title.
2.  **Series Extractor**: Extracts series/TV show entries and organizes them into `SeriesName/SeasonX/EpisodeY.strm` structure.
3.  **Live Channels Extractor**: Extracts live channel entries and saves them into a `Live_Channels` folder, grouped by category.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/silence48/m3u2strm.git
    cd m3u2strm/m3u_extractors
    ```

2.  **No special installation is required for the applications themselves**, as they are standalone Python scripts. Ensure you have Python 3 installed on your system.

## Usage

Each extractor is a command-line tool that requires an input M3U file and an output directory.

### 1. Movies Extractor

Extracts movie entries from an M3U file and organizes them.

Output structure: `OutputDirectory/Movie Title (Year)/Movie Title (Year).strm`

```bash
python3 movies_extractor/movies_extractor.py --input /path/to/your/playlist.m3u --output /path/to/your/output/movies
```

-   `--input`: Path to your M3U playlist file.
-   `--output`: Directory where the movie `.strm` files will be saved.

### 2. Series Extractor

Extracts series entries from an M3U file and organizes them.

Output structure: `OutputDirectory/Series Name/Season XX/Series Name - SXXEXX - Episode Title.strm`

```bash
python3 series_extractor/series_extractor.py --input /path/to/your/playlist.m3u --output /path/to/your/output/series
```

-   `--input`: Path to your M3U playlist file.
-   `--output`: Directory where the series `.strm` files will be saved.

### 3. Live Channels Extractor

Extracts live channel entries from an M3U file and organizes them.

Output structure: `OutputDirectory/Live_Channels/Category/Channel Name.strm`

```bash
python3 live_channels_extractor/live_channels_extractor.py --input /path/to/your/playlist.m3u --output /path/to/your/output/channels
```

-   `--input`: Path to your M3U playlist file.
-   `--output`: Directory where the live channel `.strm` files will be saved.

## Error Handling

-   The scripts will print an error message if the specified input M3U file does not exist.
-   Output directories will be created automatically if they don't exist.

## Requirements

-   Python 3.x
-   No additional dependencies are required beyond Python standard library.

## Contributing

Feel free to fork the repository, open issues, or submit pull requests.