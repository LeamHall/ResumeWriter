#!/usr/bin/env python

# name:     scrape_text_resume.py
# version:  0.0.1
# date:     20211210
# author:   Leam Hall
# desc:     Parse job section of resume to individual files.

### Notes:
#
#  1. Assumes we have a text file of just the job data. Example (no # marks):

#     DevOps Engineer (cloud), Big Corp (SubContractor) (Aug 2010 - Feb 2013) 
#
#     Did great stuff and looked really cool the entire time. Blah, blah, blah.

#  2. The header format is what I use, but needs to be configurable.

import json
import os
import re

# These need to be command line options.
job_filename    = 'data/jobs.txt'
jobs_dir        = 'data/jobs'

def write_file(data):
  ''' string, dict => writes to file
  ''' 
  try:
    file_path = os.path.join(jobs_dir, data['filename'])
    with open(file_path, 'w') as f:
      header_string = ":".join([data['title'], data['customer'],
        data['start'], data['stop'], data['key']])
      f.write("{}\n".format(header_string))
      f.write("\n{}\n".format(data['blurb']))
      f.close()
  except Exception as e:
    print(e)


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


def make_key_filename(data):
  ''' dict => strings for dict key, filename '''
  customer  = data['customer']
  customer  = re.sub("\(", '', customer)
  customer  = re.sub("\)", '', customer)
  customer  = re.sub(" ", "_", customer)
  customer  = re.sub("\.", "", customer)
  customer  = customer.lower()
  key       = "{}_{}_{}".format(data['start'], data['stop'], customer)
  filename  = "{}.txt".format(key)
  return key, filename


def parse_title_line(line):
  data              = {}
  return_line       = ''
  line_split        = line.split(",")
  data['title']     = line_split[0].strip()
  job_and_dates     = line_split[1].split("(")
  for index, item in enumerate(job_and_dates):
    job_and_dates[index] = re.sub("\)", '', item)
  customer          = job_and_dates[0].strip()
  if len(job_and_dates) > 2:
    customer = "{} ({})".format(customer, job_and_dates[1].strip())
  data['customer']  = customer
  dates             = job_and_dates[-1].strip()
  (start, stop)     = re.findall("[\d]{4}", dates)
  data['start']     = start
  data['stop']      = stop 
  return data

 
#####

ensure_write_dir(jobs_dir)

try:
  job_data  = open(job_filename, 'r')
  j_data    = {}
  for line in job_data.readlines():
    line = line.strip()
    if len(line) < 5: 
      next
    elif re.search("[\d]{4}\s*\)", line):
      j_data                    = parse_title_line(line)
      j_data['key'], j_data['filename']   = make_key_filename(j_data)
    else:
      j_data['blurb']           = line
      write_file(j_data)

except FileNotFoundError as e:
  print("Can't find file.")
  os._exit(1)


