#!/usr/bin/env python
#
# Sources header cleaner
# Currently designed only for Scala sources, you can modify as you need.
#

import os
import glob
import fnmatch


def process(file_path):
    content = []
    with open(file_path) as f:
        content = f.readlines()
    content

    found = False
    idx = 0
    for ct in content:
        idx += 1
        if ct.startswith("package"):
            found = True
            idx = idx - 1
            print ct
            break

    if found:
        content = content[idx:]
        print content

        with open(file_path, "w") as f:
            for ct in content:
                f.write(ct)


def main():

    for root, dirnames, filenames in os.walk("./"):

        for filename in fnmatch.filter(filenames, "*.scala"):
            file_path =  root + "/" + filename
            process(file_path)


if __name__ == "__main__":
    main()
