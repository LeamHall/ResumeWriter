#!/usr/bin/env python

# name:     parse_job_files.py
# version:  0.0.1
# date:     20211210
# author:   Leam Hall
# desc:     Create JSON file from numerous text files.


## Notes:
#
# Assumes a directory of files where the first line is a colon CSV of data, 
#   and the rest of the file is a blurb.

import json
import os

input_dir = "input"
json_out  = os.path.join(input_dir, "jobs.json")
data_dir  = os.path.join("data", "jobs")
json_data = {}

def make_header(line):
  datum       = {}
  header_data = line.split(":")
  header_info = ['title', 'customer', 'start', 'stop', 'key']
  for index, value in enumerate(header_data):
    datum[header_info[index]] = header_data[index]
  return datum['key'], datum
  
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

for file in os.scandir(data_dir):
  if "txt" in file.name:
    filename    = os.path.join(data_dir, file.name)
    have_header = False
    with open(filename, 'r') as f:
      lines = f.read().split("\n")
      for line in lines: 
        line = line.strip()
        if len(line) > 5 and not have_header:
          key, datum      = make_header(line)
          have_header     = True
        elif len(line):
          datum['blurb']  = line 
        json_data[key]    = datum
    f.close()



with open(json_out, 'w') as o:
  o.write(json.dumps(json_data, indent = 4))
  o.close()

