#!/usr/bin/env python3

import argparse
from gendiff import generate_diff


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file",
                        type=str,
                        help='Path to the first file.')
    parser.add_argument("second_file",
                        type=str,
                        help='Path to the second file')
    parser.add_argument("-f", "--format",
                        type=str,
                        default='stylish',
                        help="set format of output",)
    return parser.parse_args()


def main():
    args = parse_arguments()
    first_file = args.first_file
    second_file = args.second_file
    f = args.format
    print(generate_diff(first_file, second_file, f))


if __name__ == '__main__':
    main()
