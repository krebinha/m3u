import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import rawStreamList

def create_movie_files(movies, output_dir):
    for movie in movies:
        movie_title = movie.title
        year = movie.year
        if year:
            movie_title = f"{movie_title} {year}"
        movie_dir = os.path.join(output_dir, movie_title)
        os.makedirs(movie_dir, exist_ok=True)
        strm_path = os.path.join(movie_dir, f"{movie_title}.strm")
        with open(strm_path, 'w') as f:
            f.write(movie.url)

def main():
    parser = argparse.ArgumentParser(description='Extract movies from an M3U playlist.')
    parser.add_argument('--input', required=True, help='Path to the M3U file.')
    parser.add_argument('--output', required=True, help='Path to the output directory.')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found at {args.input}")
        return

    output_dir = os.path.join(args.output, "Movies")
    os.makedirs(output_dir, exist_ok=True)

    stream_list = rawStreamList(args.input)
    if 'movies' in stream_list.streams:
        create_movie_files(stream_list.streams['movies'], output_dir)
        print(f"Successfully extracted {len(stream_list.streams['movies'])} movies.")
    else:
        print("No movies found in the M3U file.")

if __name__ == '__main__':
    main()
