#!/usr/bin/env python

# name:     parse_ce.py
# version:  0.0.1
# date:     20211211
# author:   Leam Hall
# desc:     Parse a text file onto json.

### Notes:
#
# Typical line:
#
#   5399 Tractor Maintenance (Uncle Jed)

import json
import os
import re

input_dir   = "input"
data_dir    = "data"

ce_data_filename  = os.path.join(data_dir, "ce.txt")
json_filename     = os.path.join(input_dir, "ce.json")

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


### 

ce_list  = []
ensure_write_dir(input_dir)
with open(ce_data_filename, 'r') as ce_data:
  for line in ce_data.readlines():
    line = line.strip()
    m = re.match(r"([0-9]{4})\s+(.*)\s+(\(.*\))", line)
    year, course, provider = m.groups()
    provider = re.sub("\(", "", provider)
    provider = re.sub("\)", "", provider)
    ce = {"year": year, "course": course, "provider": provider }
    ce_list.append(ce)

with open(json_filename, 'w') as out:
  out.write(json.dumps(ce_list, indent = 4))
  out.close()


