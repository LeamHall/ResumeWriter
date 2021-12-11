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
resume_short_html_file_name = os.path.join(output_dir, "resume_short.html")
resume_long_html_file_name  = os.path.join(output_dir, "resume_long.html")


job_short_text  = "\n\n{title}, {customer} ({start} - {stop})"
job_long_text   = job_short_text + "\n\n{blurb}\n"
job_short_html  = "\n\n<p><b>{title}</b>  {customer} ({start} - {stop})</p>"
job_long_html   = job_short_html + "\n\n<br><br>{blurb}\n<br><br>"


# This assumes you start with a clear job section on your resume.
def write_data(filename, formatter, data):
  with open(filename, 'a') as file:
    file.write(formatter.format(**data)) 
  file.close()


###

job_keys = job_data.keys()
for job in sorted(job_keys, reverse=True):
  write_data(resume_short_text_file_name, job_short_text, job_data[job]) 
  write_data(resume_short_html_file_name, job_short_html, job_data[job]) 
  write_data(resume_long_text_file_name, job_long_text, job_data[job]) 
  write_data(resume_long_html_file_name, job_long_html, job_data[job]) 

