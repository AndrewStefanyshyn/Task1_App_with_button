#! /usr/bin/env python

import re
import sys
import subprocess
import os.path as op

def commit_msgs(start_commit, end_commit):
    return subprocess.check_output(["git",
                                    "log",
                                    "%s..%s" % (start_commit, end_commit)]).decode("utf-8")

def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write_to_file(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def format_lines(lines):
    return [("(%s)[%s]\n"%(line.split(' ', 1)[0],line.split(' ', 1)[1].split("[")[0].rstrip()))for line in lines if re.match("^http", line) is not None]

"""TODO: add shellscript"""

if __name__ == "__main__":
    import argparse
    import datetime

    parser = argparse.ArgumentParser()  
    parser.add_argument('start_commit', metavar='START_COMMIT', nargs='?')
    parser.add_argument('end_commit', metavar='END_COMMIT', nargs='?', default="HEAD")
    parser.add_argument('--inputfile', '-i',
                        help="Absolute path to input file.")
    parser.add_argument('--outfile', '-o',
                        help="Absolute path to output file.")
    args = parser.parse_args()

    if args.start_commit:
        start = args.start_commit
        end = args.end_commit
        lines = commit_msgs(start, end)
    else:
        if args.inputfile:
            filename = op.abspath(args.inputfile)
            lines = read_from_file(filename)
        else:
            print ("Specify commit range or input file name")
            exit()

    lines = format_lines(lines)
    
    if args.outfile:
        filename = op.abspath(args.outfile)
        write_to_file(filename, lines)
    else:
        print (lines)
