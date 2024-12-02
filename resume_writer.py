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

import argparse
import json
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data_dir", help="Data directory", default="data")
parser.add_argument("-o", "--output_dir", help="Output directory", default="output")
parser.add_argument("-p", "--prefix", help="filename prefix", default="resume")
parser.add_argument("-j", "--job_dir", help="Job info directory", default="jobs")
args = parser.parse_args()

output_dir      = args.output_dir
data_dir        = args.data_dir
prefix          = args.prefix
job_data_dir    = os.path.join(args.data_dir, args.job_dir)

short_text_file_name = os.path.join(output_dir, prefix + "_short.txt")
long_text_file_name  = os.path.join(output_dir, prefix + "_long.txt")
full_text_file_name  = os.path.join(output_dir, prefix + "_full.txt")
short_html_file_name = os.path.join(output_dir, prefix + "_short.html")
long_html_file_name  = os.path.join(output_dir, prefix + "_long.html")
full_html_file_name  = os.path.join(output_dir, prefix + "_full.html")

strings = { "short_text" : "", "long_text": "", "full_text":"",
    "short_html":"", "long_html":"", "full_html":"" 
    }

job_short_text  = "\n\n{title}, {customer} ({start} - {stop})"
job_long_text   = job_short_text + "\n\n{blurb}\n"
job_short_html  = "\n\n<p><b>{title}</b>    {customer} ({start} - {stop})</p>"
job_long_html   = job_short_html + "\n\n{blurb}\n<br><br>"


def write_data(filename, string):
    """
    Appends data to the file
    """
    with open(filename, 'w') as file:
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
    datafile    = os.path.join(data_dir, filename)
    if os.access(datafile, os.R_OK):
        return datafile
    else:
        raise PermissionError("{} does not exists or cannot read".format(datafile))


def continuing_edu(datafile):
    """ text data file => list of string """
    ce_list = []
    open_paren = "\\("
    close_paren = "\\)"
    with open(datafile, 'r') as data: 
        for line in data.readlines():
            line = line.strip()
            m = re.match(r"([0-9]{4})\s+(.*)\s+(\(.*\))", line)
            year, course, provider = m.groups()
            
            provider = re.sub(open_paren, "", provider)
            provider = re.sub(close_paren, "", provider)
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
    """ text data file => dict of highlights key, highlights value """
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


def single_line(datafile):
    """ text data file => string of data """
    with open(datafile, 'r') as data:
        line = data.read()
        line = line.strip()
    return line


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


if __name__ == "__main__":            
    ###
    ensure_write_dir(output_dir)

    blurb           = single_line(
                        check_datafile(data_dir, "blurb.txt"))
    ce_list         = continuing_edu(
                        check_datafile(data_dir, "ce.txt"))
    certifications  = certifications(
                        check_datafile(data_dir, "certifications.txt"))
    contact         = contact(
                        check_datafile(data_dir, "contact.txt"))
    contributions   = contributions(
                        check_datafile(data_dir, "contributions.txt"))
    education       = education(
                        check_datafile(data_dir, "edu.txt"))
    highlights      = highlights(
                        check_datafile(data_dir, "highlights.txt"))
    jobs            = jobs(job_data_dir)
    title           = single_line(
                        check_datafile(data_dir, "title.txt"))
    

    contact["blurb"] = blurb
    contact["title"] = title

    ## contact info
    contact_format_text     = "\n{name:120}{email:>30}"
    contact_format_text     += "\n{github:>150}"
    contact_format_text     += "\n{linkedin:>150}\n\n"
    contact_format_text     += "\n{blurb:120}\n\n"
    con_str_text            = contact_format_text.format(**contact)
    strings['long_text']    += con_str_text
    contact_format_html     = "<table width='100%'><tr><td align='left'><b>{name}</b></td>"
    contact_format_html     += "<td align='right'><b>{email}</b></td></tr>"
    contact_format_html     += "\n<tr><td>&nbsp</td><td align='right'><b><a href=\"{github}\">GitHub</a></b></td></tr>"
    contact_format_html     += "\n<tr><td align='left'>{blurb}</td>"
    contact_format_html     += "<td align='right'><b><a href=\"{linkedin}\">LinkedIn</a></b></td></tr>"
    contact_format_html     += "</table>\n\n"
    con_str_html            = contact_format_html.format(**contact)
    strings['long_html']    += con_str_html

    ## highlights
    strings['long_text']    += "\nRelevant Technical Skills:\n"
    #strings['long_html']    += "<h3>Relevant Technical Skills</h3>\n<ul>\n"
    strings['long_text']    += "\n"
    strings['long_html']    += "\n<ul>\n"
    highlight_format_text = "\n{}:   {}\n"
    highlight_format_html = "\n<li><b>{}</b>  {}</li>\n"
    for key, value  in highlights.items():
        strings['long_text']    += highlight_format_text.format(key, value)
        strings['long_html']    += highlight_format_html.format(key, value)


    ## experience

    strings['long_html']    += "\n</ul>\n\n"
    strings['long_text']    += "\n\nExperience:\n"
    #strings['long_html']    += "\n\n<br><h3>Experience</h3>\n\n"

    job_keys = jobs.keys()
    for job in sorted(job_keys, reverse=True):
        strings['short_text'] += job_short_text.format(**jobs[job])
        strings['long_text']  += job_long_text.format(**jobs[job])
        strings['short_html'] += job_short_html.format(**jobs[job])
        strings['long_html']  += job_long_html.format(**jobs[job])


    write_data(short_text_file_name, strings['short_text']) 
    write_data(long_text_file_name, strings['long_text']) 
    write_data(short_html_file_name, strings['short_html']) 
    write_data(long_html_file_name, strings['long_html']) 

