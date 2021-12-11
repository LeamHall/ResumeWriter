#!/usr/bin/env python

# name:     parse_edu.py
# version:  0.0.1
# date:     20211211
# author:   Leam Hall
# desc:     Parses Education data into json.

## Notes:
#
# Typical line:
#
#   Associate of Science, Moisture Vaporators, On-line College, Tatoonie, 5399


import json
import os

input_dir   = "input"
data_dir    = "data"
edu_file    = os.path.join(data_dir, "edu.txt")
json_file   = os.path.join(input_dir, "edu.json")

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
edu_list = []

with open(edu_file, 'r') as in_file:
  for line in in_file.readlines():
    edu                 = {}
    line                = line.strip()
    level, topic, institution, location, year = line.split(",")
    edu['level']        = level.strip()
    edu['topic']        = topic.strip()
    edu['institution']  = institution.strip()
    edu['location']     = location.strip()
    edu['year']         = year.strip()    
    edu_list.append(edu)
in_file.close()

with open(json_file, 'w') as out:
  out.write(json.dumps(edu_list, indent = 4))
  out.close

