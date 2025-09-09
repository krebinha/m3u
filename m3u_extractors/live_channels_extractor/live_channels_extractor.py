import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import rawStreamList

def create_live_channel_files(channels, output_dir):
    for channel in channels:
        category = channel.group if channel.group else "Uncategorized"
        category_dir = os.path.join(output_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        
        channel_title = channel.title.replace(':','-').replace('*','_').replace('/','_').replace('?','')
        strm_path = os.path.join(category_dir, f"{channel_title}.strm")
        with open(strm_path, 'w') as f:
            f.write(channel.url)

def main():
    parser = argparse.ArgumentParser(description='Extract live channels from an M3U playlist.')
    parser.add_argument('--input', required=True, help='Path to the M3U file.')
    parser.add_argument('--output', required=True, help='Path to the output directory.')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found at {args.input}")
        return

    output_dir = os.path.join(args.output, "Live_Channels")
    os.makedirs(output_dir, exist_ok=True)

    stream_list = rawStreamList(args.input)
    if 'live' in stream_list.streams:
        create_live_channel_files(stream_list.streams['live'], output_dir)
        print(f"Successfully extracted {len(stream_list.streams['live'])} live channels.")
    else:
        print("No live channels found in the M3U file.")

if __name__ == '__main__':
    main()
