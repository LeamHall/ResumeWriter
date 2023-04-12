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

output_dir      = "output"
data_dir        = "data"
job_data_dir    = os.path.join(data_dir, "jobs")

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
job_short_html  = "\n\n<p><b>{title}</b>    {customer} ({start} - {stop})</p>"
job_long_html   = job_short_html + "\n\n{blurb}\n<br><br>"


def write_data(filename, string):
    """
    Appends data to the file
    """
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
    datafile    = os.path.join(data_dir, filename)
    if os.access(datafile, os.R_OK):
        return datafile
    else:
        raise PermissionError("{} does not exists or cannot read".format(datafile))

if __name__ == "__main__":            
    ###
    ensure_write_dir(output_dir)
    for file in os.scandir(output_dir):
        os.remove(file)

    ce_list         = parsers.continuing_edu(
                        check_datafile(data_dir, "ce.txt"))
    certifications  = parsers.certifications(
                        check_datafile(data_dir, "certifications.txt"))
    contact         = parsers.contact(
                        check_datafile(data_dir, "contact.txt"))
    contributions   = parsers.contributions(
                        check_datafile(data_dir, "contributions.txt"))
    education       = parsers.education(
                        check_datafile(data_dir, "edu.txt"))
    highlights      = parsers.highlights(
                        check_datafile(data_dir, "highlights.txt"))
    jobs            = parsers.jobs(job_data_dir)


    ## contact info
    contact_format_text     = "\n{name:30}{email:>30}\n{github:>60}"
    contact_format_text     += "\n{linkedin:>60}\n\n"
    con_str_text            = contact_format_text.format(**contact)
    strings['long_text']    += con_str_text
    contact_format_html     = "<table width='100%'><tr><td align='left'><b>{name}</b></td>"
    contact_format_html     += "<td align='right'><b>{email}</b></td></tr>"
    contact_format_html     += "\n<tr><td>&nbsp</td><td align='right'><b><a href=\"{github}\">GitHub</a></b></td></tr>"
    contact_format_html     += "\n<tr><td align='left'></td>"
    contact_format_html     += "<td align='right'><b><a href=\"{linkedin}\">LinkedIn</a></b></td></tr>"
    contact_format_html     += "</table>\n\n"
    con_str_html            = contact_format_html.format(**contact)
    strings['long_html']    += con_str_html

    ## highlights
    strings['long_text']    += "\nRelevant Technical Skills\n"
    strings['long_html']    += "<h3>Relevant Technical Skills</h3>\n<ul>\n"
    highlight_format_text = "\n{}   {}\n"
    highlight_format_html = "\n<li><b>{}</b>  {}</li>\n"
    for key, value  in highlights.items():
        strings['long_text']    += highlight_format_text.format(key, value)
        strings['long_html']    += highlight_format_html.format(key, value)


    ## experience

    strings['long_html']    += "\n</ul>\n\n"
    strings['long_text']    += "\n\nExperience\n"
    strings['long_html']    += "\n\n<br><h3>Experience</h3>\n\n"

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

