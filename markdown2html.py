#!/usr/bin/python3
""" change markdown to html """
import sys
import os


if __name__ == '__main__':
    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    # Store the arguments into variables
    markDownFile = sys.argv[1]
    htmlFile = sys.argv[2]

    # Checks that the markdown file exists and is a file
    if not (os.path.exists(markDownFile) and os.path.isfile(markDownFile)):
        print(f'Missing {markDownFile}', file=sys.stderr)
        exit(1)
    exit(0)
