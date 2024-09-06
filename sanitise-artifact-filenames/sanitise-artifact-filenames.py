#!/usr/bin/python3

"""
This script sanitises directory and file names for GitHub Actions artifacts.
Example error from the upload-artifact action if you have an invalid path:

  Error: The path for one of the files in artifact is not valid:
  /tempest-artifacts.2024-08-29T18:18+00:00/docker.log. Contains the following
  character:  Colon :
            
  Invalid characters include:  Double quote ", Colon :, Less than <, Greater than
  >, Vertical bar |, Asterisk *, Question mark ?, Carriage return \r, Line feed
  \n
            
  The following characters are not allowed in files that are uploaded due to
  limitations with certain file systems such as NTFS. To maintain file system
  agnostic behavior, these characters are intentionally not allowed to prevent
  potential problems with downloads on different file systems.
"""

import os
import sys
import typing as t


def main() -> None:
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    sanitise(sys.argv[1])


def usage() -> None:
    print(f"Usage: {sys.argv[0]} <path>")


def sanitise(path: str) -> None:
    # Recursively walk a directory, sanitising subdirectories and files as we go.
    # Walk bottom-up to avoid directory renames breaking subsequent paths.
    table = translation_table()
    for dirpath, dirnames, filenames in os.walk(path, topdown=False, followlinks=False):
        for filename in filenames:
            sanitise_file_or_dir(filename, table, dirpath)
        for dirname in dirnames:
            sanitise_file_or_dir(dirname, table, dirpath)


def translation_table() -> t.Dict:
    # Return a translation table that translates all disallowed characters to a dash.
    disallowed = "\":<>|*?\r\n"
    return str.maketrans(disallowed, "-" * len(disallowed))


def sanitise_file_or_dir(path: str, table: t.Dict, dirpath: str) -> None:
    # Sanitise a single file or directory.
    sanitised = path.translate(table)
    if path != sanitised:
        print(f"Sanitising {path} as {sanitised} in {dirpath}")
        path = os.path.join(dirpath, path)
        dirpath = os.path.join(dirpath, sanitised)
        os.rename(path, dirpath)


if __name__ == "__main__":
    main()
