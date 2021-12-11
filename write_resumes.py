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

resume_short_text_file = os.path.join(output_dir, "resume_short.txt")
resume_long_text_file  = os.path.join(output_dir, "resume_long.txt")
resume_short_html_file = os.path.join(output_dir, "resume_short.html")
resume_long_html_file = os.path.join(output_dir, "resume_long.html")


job_short_text  = "\n\n{}, {} ({} - {})"
job_long_text   = job_short_text + "\n\n{}\n"
job_short_html  = "\n\n<p><b>{}</b>  {} ({} - {})</p>"
job_long_html   = job_short_html + "\n\n<br><br>{}\n<br><br>"

resume_short_text_file  = open(resume_short_text_file, 'w')
resume_long_text_file   = open(resume_long_text_file, 'w')
resume_short_html_file  = open(resume_short_html_file, 'w')
resume_long_html_file   = open(resume_long_html_file, 'w')

class Job:

  def __init__(self, data):
    self.title = data['title']
    self.customer = data['customer']
    self.start    = data['start']
    self.stop     = data['stop']
    self.blurb    = data['blurb']

def write_data(file, formatter):
  file.write(formatter) 

#print(json.dumps(job_data, indent = 2))
job_keys = job_data.keys()
for job in sorted(job_keys, reverse=True):
  j = Job(job_data[job])

  write_data(resume_short_text_file, 
    job_short_text.format(j.title, j.customer, j.start, j.stop))
  write_data(resume_long_text_file, 
    job_long_text.format(j.title, j.customer, j.start, j.stop, j.blurb))
  write_data(resume_short_html_file, 
    job_short_html.format(j.title, j.customer, j.start, j.stop))
  write_data(resume_long_html_file, 
    job_long_html.format(j.title, j.customer, j.start, j.stop, j.blurb))

