#!/usr/bin/env python2

# hashfs module - store large ammount of files on the file system

import os
import md5
import uuid
import sys
import argparse

def initfs(folder, maxlevel, level = 1):
    if level > maxlevel:
        return

    names = list("0123456789abcdef")

    for name in names:
        current = folder + "/" + name
        os.mkdir( current )
        initfs( current, maxlevel, level + 1 )

def get_path(name, maxlevel, keep_name = True):
    m = md5.new()
    m.update(name)
    return "/".join( m.hexdigest()[:maxlevel] ) + "/" + ( name if keep_name else str(uuid.uuid4()) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='hasfs - store large ammount of files in a directory')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-d', '--dir', help='hashfs source directory', required=True)
    args = parser.parse_args()

    # initialize directories
    dir = args.dir
    if not os.path.isdir(dir):
        print "invalid directory: " + dir
        sys.exit(1)

    initfs(dir, 3 )

    sys.exit(0)
