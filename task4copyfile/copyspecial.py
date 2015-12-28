#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
##/usr/bin/env python3
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
import codecs

"""Copy Special exercise
"""
def copy_to():
  dir = os.getcwd()
  p = subprocess.Popen('ls ' + dir + ' |grep "__\w\+__"', shell = True, stdout = subprocess.PIPE)
  for line in p.stdout:
    #from pdb import set_trace
    #set_trace() 
    print(line[0:-1].encode('utf-8'))
    subprocess.Popen('cp '+line[0:-1]+' new'+line[0:-1], shell = True, stdout = subprocess.PIPE)

def to_zip(filename):
  dir = os.getcwd()
  p = subprocess.Popen('ls ' + dir + ' |grep ' + filename + '', shell = True, stdout = subprocess.PIPE)
  for line in p.stdout:
    #from pdb import set_trace
    #set_trace() 
    print(line[0:-1].encode('utf-8'))
    #from pdb import set_trace
    #set_trace() 
    subprocess.Popen('zip -r newzip' + line[0:-1], shell = True, stdout = subprocess.PIPE)
  #return 0
# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--todir':
    copy_to()
  elif option == '--tozip':
    to_zip(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
