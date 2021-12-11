#!/usr/bin/env python

# name:     parse_contributions.py
# version:  0.0.1
# date:     20211211
# author:   Leam Hall
# desc:     Parses Contribution data into json.

## Notes:
#
# Typical line:
#
#   Visual Basic Document  https://ihatetatoonie.net/contributions


import json
import os

input_dir   = "input"
data_dir    = "data"
edu_file    = os.path.join(data_dir, "open_source_contributions.txt")
json_file   = os.path.join(input_dir, "open_source_contributions.json")

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
contrib_list = []

with open(edu_file, 'r') as in_file:
  for line in in_file.readlines():
    contrib         = {}
    line            = line.strip()
    line_data       = line.split(" ")
    info_string     = " ".join(line_data[:-1])
    contrib['url']  = line_data[-1].strip()
    contrib['info'] = info_string.strip()
    contrib_list.append(contrib)
in_file.close()

with open(json_file, 'w') as out:
  out.write(json.dumps(contrib_list, indent = 4))
  out.close
