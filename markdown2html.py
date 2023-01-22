#!/usr/bin/python3
""" change markdown to html """
import sys
import os
import re


if __name__ == '__main__':
    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    # Store the arguments into variables
    markDownFile = sys.argv[1]
    htmlFile = sys.argv[2]

    if not (os.path.exists(markDownFile) and os.path.isfile(markDownFile)):
        print(f'Missing {markDownFile}', file=sys.stderr)
        exit(1)
    with open(markDownFile, encoding='utf-8') as mFile:
        htmlContent = []
        mdContent = [line[:-1] for line in mFile.readlines()]
        for line in mdContent:
            line = line.replace('**', '<b>', 1)
            line = line.replace('**', '</b>', 1)
            line = line.replace('__', '<em>', 1)
            line = line.replace('__', '</em>', 1)
            line = line.replace('-', '<li>', 1)
            heading = re.split(r'#{1,6} ', line)
            if len(heading) > 1:
                h_level = len(line[:line.find(heading[1])-1])
                htmlContent.append(
                    f'<h{h_level}>{heading[1]}</h{h_level}>\n'
                )
            else:
                htmlContent.append(line)

    with open(htmlFile, 'w', encoding='utf-8') as file_2:
        file_2.writelines(htmlContent)
