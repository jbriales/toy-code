#!/usr/bin/env python3
# coding=utf-8
"""
Check various features of the argparse package
"""

import argparse
from pprint import pprint

if __name__ == '__main__':
    # The main parser
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument('-f', '--foo', '--do_foo', '--do-foo', '--another', action='store_true',
                        help="a true flag")
    parser.add_argument('--do_bar', '--bar', '-b', '-a', action='store_true',
                        help="a true flag")
    # Main name non-valid Python identifier: - is turned into _ automatically in args
    parser.add_argument('--do-quz', '--quz', action='store_true',
                        help="a true flag")
    # Mixed positional and optional names: Will crash
    # parser.add_argument('--do-quz', 'pos', action='store_true', help="a true flag")

    # Parse arguments
    args = parser.parse_args()

    # Display args
    pprint(vars(args))
