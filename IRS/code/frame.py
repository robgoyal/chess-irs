import argparse
import subprocess

from pprint import pprint
from board import Board


class Frame:

    def __init__(self, args):
        self.input_path = args.input
        self.output_path = args.output

    def process_image(self):
        args = ['python', '/Users/robing/Documents/Projects/GitHub/OpenCVChess/IRS/code/neural_chessboard/main.py', 'detect', '--input', self.input_path,
                '--output', self.output_path]
        p = subprocess.run(args, stderr=subprocess.STDOUT)

    def get_output_path(self):
        return self.output_path


if __name__ == "__main__":
    p = argparse.ArgumentParser(description= \
                                    'Find, crop and create FEN from image.')

    p.add_argument('--input', type=str, \
                   help='input image (default: input.jpg)')
    p.add_argument('--output', type=str, \
                   help='output path (default: output.jpg)')

    args = p.parse_args()

    f = Frame(args)
    f.process_image()

    b = Board(f.output_path, f.input_path)
    pprint(b.get_piece_locations())
