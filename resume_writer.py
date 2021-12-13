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

import parsers.parsers as parsers

output_dir  = "output"
data_dir    = "data"
job_data_dir  = os.path.join(data_dir, "jobs")

resume_short_text_file_name = os.path.join(output_dir, "resume_short.txt")
resume_long_text_file_name  = os.path.join(output_dir, "resume_long.txt")
resume_full_text_file_name  = os.path.join(output_dir, "resume_full.txt")
resume_short_html_file_name = os.path.join(output_dir, "resume_short.html")
resume_long_html_file_name  = os.path.join(output_dir, "resume_long.html")
resume_full_html_file_name  = os.path.join(output_dir, "resume_full.html")

strings = { "short_text" : "", "long_text": "", "full_text":"",
  "short_html":"", "long_html":"", "full_html":"" 
  }

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

def check_datafile(data_dir, filename):
  datafile  = os.path.join(data_dir, filename)
  if os.access(datafile, os.R_OK):
    return datafile
  else:
    raise PermissionError("{} does not exists or cannot read".format(datafile))
    
###
ensure_write_dir(output_dir)
for file in os.scandir(output_dir):
  os.remove(file)

ce_list         = parsers.continuing_edu(check_datafile(data_dir, "ce.txt"))
certifications  = parsers.certifications(check_datafile(data_dir, "certifications.txt"))
contact         = parsers.contact(check_datafile(data_dir, "contact.txt"))
contributions   = parsers.contributions(check_datafile(data_dir, "contributions.txt"))
education       = parsers.education(check_datafile(data_dir, "edu.txt"))
highlights      = parsers.highlights(check_datafile(data_dir, "highlights.txt"))
jobs            = parsers.jobs(job_data_dir)


job_keys = jobs.keys()
for job in sorted(job_keys, reverse=True):
  strings['short_text'] += job_short_text.format(**jobs[job])
  strings['long_text']  += job_long_text.format(**jobs[job])
  strings['short_html'] += job_short_html.format(**jobs[job])
  strings['long_html']  += job_long_html.format(**jobs[job])


write_data(resume_short_text_file_name, strings['short_text']) 
write_data(resume_long_text_file_name, strings['long_text']) 
write_data(resume_short_html_file_name, strings['short_html']) 
write_data(resume_long_html_file_name, strings['long_html']) 

