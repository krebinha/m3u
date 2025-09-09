import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import rawStreamList

def create_series_files(series, output_dir):
    # Helper function to sanitize strings for directory and file names
    def sanitize_name(name):
        if not isinstance(name, str):
            name = str(name)
        return name.replace(':', '-').replace('*', '_').replace('/', '_').replace('?', '')

    # Iterate over each episode extracted from the M3U file
    for i, episode in enumerate(series):
        # Determine the streaming platform from the group title, default to "Uncategorized"
        platform = getattr(episode, 'group', "Uncategorized")
        if not platform:
            platform = "Uncategorized"
        
        # Sanitize platform and series title for path creation
        sanitized_platform = sanitize_name(platform)
        sanitized_show_title = sanitize_name(episode.showtitle)

        # Define the directory structure: OutputDirectory/StreamingPlatform/SeriesName
        series_dir = os.path.join(output_dir, sanitized_platform, sanitized_show_title)
        
        # Create the directories if they don't exist
        os.makedirs(series_dir, exist_ok=True)

        # Determine the episode file name
        if episode.episodenumber:
            # Format as "Episode X.strm" if episode number is available
            episode_filename = f"Episode {episode.episodenumber}.strm"
        elif episode.episodename:
            # Use the sanitized episode name if number is not available
            episode_filename = f"{sanitize_name(episode.episodename)}.strm"
        else:
            # As a fallback, use a generic name with an index
            episode_filename = f"Episode {i + 1}.strm"
        
        # Construct the full path for the .strm file
        strm_path = os.path.join(series_dir, episode_filename)
        
        # Write the stream URL to the .strm file
        with open(strm_path, 'w') as f:
            f.write(episode.url)

def main():
    parser = argparse.ArgumentParser(description='Extract series from an M3U playlist.')
    parser.add_argument('--input', required=True, help='Path to the M3U file.')
    parser.add_argument('--output', required=True, help='Path to the output directory.')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found at {args.input}")
        return

    output_dir = os.path.join(args.output, "Series")
    os.makedirs(output_dir, exist_ok=True)

    stream_list = rawStreamList(args.input)
    if 'series' in stream_list.streams:
        create_series_files(stream_list.streams['series'], output_dir)
        print(f"Successfully extracted {len(stream_list.streams['series'])} series episodes.")
    else:
        print("No series found in the M3U file.")

if __name__ == '__main__':
    main()
