# ResumeWriter
Provides resumes in different output formats.

When you're job searching, you have to have a resume or CV to share with 
potential employers. Listening to their questions as feedback on your 
resume will let you tailor it for the next interview. This is an 
on-going process.

What makes this more difficult is that you need a standard word processor
version in docx format, as well as a PDF version. You want a website that
has HTML markup, and a text version helps when formatting is problematic.

It is also handy to have a short version with just the job title, company,
and dates; this can generate interest for longer versions and conversations.

Keeping all of these is sync is a pain. Hopefully the tools here will help
east that pain a little.

## Getting the initial data

Assuming you cut and paste a text version of your jobs into data/jobs.txt, 
and then run:

    scrape_text_resume.py

This will break each job into a single file, in data/jobs. For example:

    $ cat data/jobs/5382_5400_tatoonie.txt

    Farm Hand:Tatoonie:5382:5400:5382_5400_tatoonie

    Working the family farm; harvesting dirt. Highly successful.

You can then keep the jobs in version control, and edit just what you need
to edit, based on feedback and career goals. The first line, starting
"Farm Hand", is a colon separated file with:

  Job Title:Customer:Start Date:End Date:dict_key_based_on_dates_and_customer

There are also files for continuing education ("ce.txt"), certifications 
("certifications.txt"), education ("edu.txt"), career highlights
("highlights.txt), and open source contributions ("contributions.txt").

Copy the "sample_data/" directory to "data/" to see what happens.


## Writing the job resume stuff

    resume_writer.py

Okay, yes. There are much better templating systems out there. I tend to use
the standard library. You may want to alter the formatters, and when I figure 
out a good templating system I will add it. 

Anyway, resume_writer.py takes the text files and writes varous versions in 
both text and HTML. The short version is just the job header information, the 
long version includes the blurb and other stuff. I tend to use the HTML version
to import into a word processer to create both docx and PDF formats.


## Future State

Lots to do, but I also have to get back to my job search. This ain't academic.




