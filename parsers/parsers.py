# name:     parsers.py
# version:  0.0.1
# date:     20211213
# author:   Leam Hall
# desc:     Parses text files to data structures.

##

import os
import re

def continuing_edu(datafile):
    """ text data file => list of string """
    ce_list = []
    with open(datafile, 'r') as data: 
        for line in data.readlines():
            line = line.strip()
            m = re.match(r"([0-9]{4})\s+(.*)\s+(\(.*\))", line)
            year, course, provider = m.groups()
            provider = re.sub("\(", "", provider)
            provider = re.sub("\)", "", provider)
            ce = {"year": year, "course": course, "provider": provider }
            ce_list.append(ce)
    
    return ce_list


def certifications(datafile):
    """ text data file => list of string """
    cert_list = [] 
    with open(datafile, 'r') as data:
        for line in data.readlines():
            line = line.strip()
            cert_list.append(line)
    return cert_list


def contact(datafile):
    """ text data file => dict of contact key, contact value """
    contact = {}
    with open(datafile, 'r') as data:
        for line in data.readlines():
            line = line.strip()
            if len(line) < 5:
                continue
            key, value    = line.split(" ", maxsplit = 1)
            key           = key.strip()
            value         = value.strip()
            contact[key]  = value
    return contact


def contributions(datafile):
    """ text data file => list of string """
    contribs = []
    with open(datafile, 'r') as data:
        for line in data.readlines():
            line            = line.strip()
            line_data       = line.split(" ")
            info_string     = " ".join(line_data[:-1])
            contrib         = {}
            contrib['url']  = line_data[-1].strip()
            contrib['info'] = info_string.strip()
            contribs.append(contrib)
    return contribs


def education(datafile):
    """ text data file => list of string """
    education = []
    with open(datafile, 'r') as data:
        for line in data.readlines():
            line                = line.strip()
            level, topic, institution, location, year = line.split(",")
            edu                 = {}
            edu['level']        = level.strip()
            edu['topic']        = topic.strip()
            edu['institution']  = institution.strip()
            edu['location']     = location.strip()
            edu['year']         = year.strip()    
            education.append(edu)
    return education


def highlights(datafile):
    """ text data file => dict of contact key, contact value """
    highlights = {}
    with open(datafile, 'r') as data:
        for line in data.readlines():
            line = line.strip()
            if len(line) < 5:
                continue
            key, value      = line.split(":")
            key             = key.strip()
            value           = value.strip()
            highlights[key] = value
    return highlights


def make_job_header(line):
    """ data line => string, dict """
    datum       = {}
    header_data = line.split(":")
    header_info = ['title', 'customer', 'start', 'stop', 'key']
    for index, value in enumerate(header_data):
        datum[header_info[index]] = header_data[index]
    return datum['key'], datum


def jobs(data_dir):
    """ directory of data files => dict of dicts """
    jobs = {}
    for file in os.scandir(data_dir):
        if "txt" in file.name:
            filename    = os.path.join(data_dir, file.name)
            have_header = False
            with open(filename, 'r') as f:
                lines = f.read().split("\n")
                for line in lines: 
                    line = line.strip()
                    if len(line) > 5 and not have_header:
                        key, datum      = make_job_header(line)
                        have_header     = True
                    elif len(line):
                        datum['blurb']  = line 
                    jobs[key]    = datum
    return jobs


