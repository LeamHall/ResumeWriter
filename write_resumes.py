#!/usr/bin/env python

# name:     write_resumes.py
# version:  0.0.1
# date:     20211210
# author:   Leam Hall
# desc:     Pulls json files and writes various resume types.

## Notes:
#
#  1. Really needs to use resume templates, but I don't want to go 
#       outside of the standard library.

import json
import os

input_dir   = "input"
output_dir  = "output"
job_file    = os.path.join(input_dir, "jobs.json")
data        = open(job_file, 'r').read()
job_data    = json.loads(data)

resume_short_text_file_name = os.path.join(output_dir, "resume_short.txt")
resume_long_text_file_name  = os.path.join(output_dir, "resume_long.txt")
resume_full_text_file_name  = os.path.join(output_dir, "resume_full.txt")
resume_short_html_file_name = os.path.join(output_dir, "resume_short.html")
resume_long_html_file_name  = os.path.join(output_dir, "resume_long.html")
resume_full_html_file_name  = os.path.join(output_dir, "resume_full.html")

string_short_text   = ""
string_long_text    = ""
string_full_text    = ""
string_short_html   = ""
string_long_html    = ""
string_full_html    = ""

job_short_text  = "\n\n{title}, {customer} ({start} - {stop})"
job_long_text   = job_short_text + "\n\n{blurb}\n"
job_short_html  = "\n\n<p><b>{title}</b>  {customer} ({start} - {stop})</p>"
job_long_html   = job_short_html + "\n\n<br><br>{blurb}\n<br><br>"


def write_data(filename, string):
  with open(filename, 'a') as file:
    file.write(string)
  file.close()

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
ensure_write_dir(output_dir)
for file in os.scandir(output_dir):
  os.remove(file)

job_keys = job_data.keys()
for job in sorted(job_keys, reverse=True):
  string_short_text += job_short_text.format(**job_data[job])
  string_long_text  += job_long_text.format(**job_data[job])
  string_short_html += job_short_html.format(**job_data[job])
  string_long_html  += job_long_html.format(**job_data[job])

write_data(resume_short_text_file_name, string_short_text) 
write_data(resume_long_text_file_name, string_long_text) 
write_data(resume_short_html_file_name, string_short_html) 
write_data(resume_long_html_file_name, string_long_html) 

