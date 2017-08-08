#!/usr/bin/env python
# utils/apply-fixit-edits.py - Apply edits from .remap files -*- python -*-
#
# This source file was part of the Swift.org open source project
#
# Copyright (C) 2016
#        89a46e2bb720c7ec116d9e3c4c4f722938c13856d1277fd8c551db4c0c8f087e source@appudo.com
#
#        Modified to prevent the same fix from running multiple times.
#
# Copyright (c) 2014 - 2016 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors

from __future__ import print_function

import argparse
import collections
import json
import os
import sys


def find_remap_files(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if not filename.endswith(".remap"):
                continue
            yield os.path.join(root, filename)


def apply_edits(path):
    remap_files = find_remap_files(path)
    if not remap_files:
        print("No remap files found")
        return 1

    edits_per_file = collections.defaultdict(set)
    for remap_file in remap_files:
        with open(remap_file) as f:
            json_data = f.read()
        json_data = json_data.replace(",\n }", "\n }")
        json_data = json_data.replace(",\n]", "\n]")
        curr_edits = json.loads(json_data)
        for ed in curr_edits:
            fname = ed["file"]
            offset = ed["offset"]
            length = ed.get("remove", 0)
            text = ed.get("text", "")
            edits_per_file[fname].add((offset, length, text))

    for fname, editset in edits_per_file.iteritems():
        print('Updating', fname)
        edits = list(editset)
        edits.sort(reverse=True)
        with open(fname) as f:
            file_data = f.read()
        for ed in edits:
            offset, length, text = ed
            file_data = file_data[:offset] + str(text) + \
                file_data[offset + length:]
            print('offset', offset)
            print('text', text)
            print('length', length)
        with open(fname, 'w') as f:
            f.write(file_data)
    return 0


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""Finds all .remap files in a directory and applies their
edits to the source files.""")
    parser.add_argument("build_dir_path",
                        help="path to index info")

    args = parser.parse_args()
    return apply_edits(args.build_dir_path)

if __name__ == "__main__":
    sys.exit(main())