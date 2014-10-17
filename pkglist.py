#!/usr/bin/env python
"""
USAGE:
pkglist.py -h
Writing repos to a file.
"""

import argparse
import os
import re
import sys

hashre = re.compile('^[a-z0-9]+$')

def check_args():
    '''Checks arguments
       Returns object with all of it'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-al', '--all-logs', metavar=('PROJECT'), nargs='+', help='Get all logs')
    parser.add_argument('-q', '--quite', metavar=('PROJECT'), nargs='+', help='Make quite')

    if not len(sys.argv) > 1:
        parser.print_help()

    try:
        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    return args

if __name__ == "__main__":
    args = check_args()

    if args.update:
        [git_pull(i) for i in args.update]
    if args.all_logs:
        [git_log(i) for i in args.all_logs]
