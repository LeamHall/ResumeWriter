#!/usr/bin/env python

import re
import os

datadir = "data"
ce_text_string = "{} {} {}\n"
ce_html_string = "<p><b>{}</b> {} {}</p>\n"
ce_file = "continuing_education.txt"
### Sample lines (no '#'):
# Python:
#  Learn to Program, The Fundamentals (Python) (Coursera) (January 2014)

ce_text_out = 'ce.txt'
ce_html_out = 'ce.html'
ce_text_fh = open(ce_text_out, 'w')
ce_html_fh = open(ce_html_out, 'w')

class ContEd():
  def __init__(self, dataline):
    parts = dataline.split(" ")
    self.year = parts[-1].replace(')','')
    self.source = parts[-3]
    self.course = " ".join(parts[:-3])


def cont_ed_out(ce, format_string, filehandle):
  filehandle.write(format_string.format(ce.year, ce.course, ce.source))

def list_from_file(directory, file):
  filename	= os.path.join(datadir, file)
  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  data = [] 
  for line in lines:
	  line = line.strip()
	  if len(line):
	    data.append(line) 
  return data

def sorted_list(data, sort_attrib, direction = False):
  stuff = {}
  return_list = []
  for d in data:
    # need a way to translate the sort_attrib to "year".
    K = d.year
    if K not in stuff.keys():
      stuff[K] = []
    stuff[K].append(d)
  
  for my_k in sorted(stuff.keys(), reverse = True):
    my_sorted_list = sorted(stuff[my_k], key=lambda ce: ce.course) 
    return_list.extend(my_sorted_list)
  return return_list


ce_data_file = list_from_file(datadir, ce_file)
ce_data = []
for l in ce_data_file:
  if re.search('[0-9]{4}', l):
    ce = ContEd(l)	
    ce_data.append(ce) 


rev_sorted_ce = sorted_list(ce_data, 'year')
for ce in rev_sorted_ce:
  cont_ed_out(ce, ce_text_string, ce_text_fh)
  cont_ed_out(ce, ce_html_string, ce_html_fh)
 
ce_text_fh.close()
ce_html_fh.close()
 
