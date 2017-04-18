import re
import sys
import subprocess

def commit_msgs(revision_range):
    out = subprocess.check_output(["git", "rev-list", "--format=%B", revision_range])
    return out.decode("utf-8")

if __name__ == "__main__":

    lines = list(filter(bool, re.split(r'\s*commit \w+\n', commit_msgs("--all"))))
    print (lines)
