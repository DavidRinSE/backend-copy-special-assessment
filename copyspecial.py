#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import sys
import shutil
import subprocess
import argparse

__author__ = "DavidRinSE"

def get_special_paths(directory):
    regex = re.compile('__(.*?)__')
    filenames = []
    for _, _, files in os.walk(directory, topdown=False):
        for name in files:
            if regex.search(name):
                filenames.append(os.path.abspath(name))
    return filenames

def copy_to(paths, copypath):
    for path in paths:
        try:
            shutil.copy(path, copypath)
        except:
            os.makedirs(os.path.abspath(copypath))
            shutil.copy(path, copypath)

def zip_to(paths, zippath):
    command = "zip -j {} {}".format(zippath, " ".join(paths))
    print("Command I'm going to do:\n{}".format(command))
    check = subprocess.check_output(
        command + "; exit 0",
        stderr=subprocess.STDOUT,
        shell=True)
    print('\n' + str(check, 'utf-8'))

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='search dir for special files')
    ns = parser.parse_args(args)
    
    if not ns:
        parser.print_usage()
        sys.exit(1)

    special_paths = get_special_paths(ns.fromdir)
    
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    
    if not ns.todir and not ns.tozip:
        for path in special_paths:
            print(path)

if __name__ == "__main__":
    main(sys.argv[1:])
