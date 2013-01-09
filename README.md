# Overview

My [resume](http://ceasar.github.com/resume/), managed with Git, styled with Bootstrap.

## Features

- Fluid layout
- Print button in screen version
- Dynamic access and update date
- Data separated from html

# Installation

`pip install -r requirements.txt`

# Quickstart

To compile the templates into the resume, run `python build.py`. This will automatically watch the templates for changes and rebuild the resume on change.

My ruby is a little weak, but to compile the sass to css requires [compass](http://compass-style.org/) (this is because the sass requires bootstrap-sass which requires compass). Once installed, run `compass watch static` and it will watch for any changes and update the css accordingly.

# Converting to PDF

To convert the web page to a PDF, the best way I've found is just to print to PDF (making sure to uncheck headers and footers). A print button is on the screen version of the resume for convenience.
