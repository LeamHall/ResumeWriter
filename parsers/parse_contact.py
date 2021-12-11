#!/usr/bin/env python

# name:     parse_contact.py
# version:  0.0.1
# date:     20211211
# author:   Leam Hall
# desc:     Parse a text file onto json.

## Notes:
#
# Run from project base directory.
#
# Typical file (the first "word" should be a valid dict key):
#   If you create your own templates then you can add whatever keys you need.
#
#   name      Luke Skywalker
#   phone     555.555.1212
#   linkedin  https://linkedin.com/LSkywalker
#   github    https://github.com/ihatetatoonie

import json
import os
import re

input_dir   = "input"
json_file   = os.path.join(input_dir, "contact.json")
data_dir    = "data"
data_file   = os.path.join(data_dir, "contact.txt")

def ensure_write_dir(directory):
  ''' directory name => creates if not exist, verifies dir and writeable.
    else raise exception.
  '''
  if not os.path.isdir(directory):
    try:
      os.mkdir(directory, 0o0755)
    except OSError as ose:
      print("Cannot create directory")
      os._exit(1)


####

ensure_write_dir(input_dir)

contact = {}
with open(data_file, 'r') as c:
  for line in c.readlines():
    line = line.strip()
    if len(line) < 5:
      continue
    key, value    = line.split(" ", maxsplit = 1)
    key           = key.strip()
    value         = value.strip()
    contact[key]  = value

with open(json_file, 'w') as out:
  out.write(json.dumps(contact, indent = 4))
  out.close()

