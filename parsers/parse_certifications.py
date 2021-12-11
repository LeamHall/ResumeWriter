#!/usr/bin/env python

# name:     parse_certifications.py
# version:  0.0.1
# date:     20211211
# author:   Leam Hall
# desc:     Parses Certification data into json.

## Notes:
#
# Typical line:
#
#   Dirt Sorting (Level 1)


import json
import os

input_dir   = "input"
data_dir    = "data"
cert_file   = os.path.join(data_dir, "certifications.txt")
json_file   = os.path.join(input_dir, "certifications.json")

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

ensure_write_dir(input_dir)
cert_list = []

with open(cert_file, 'r') as in_file:
  for line in in_file.readlines():
    line = line.strip()
    cert_list.append(line)
in_file.close()

with open(json_file, 'w') as out:
  out.write(json.dumps(cert_list, indent = 4))
  out.close

