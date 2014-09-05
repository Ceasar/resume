# Overview

An attempt to make a modular resume that is easy to maintain.

## Features

- Fluid layout
- Download button in screen version
- Dynamic access date and update date
- Data separated from presentation

# Quickstart

To generate the resume, simply run:

```
make
```

## Data

The resume is meant to be completely modular, so no personal data is embedded
directly in the HTML. Instead, data is stored inside of `data/` and embedded
using Javascript and Jinja2.

The following files are necessary to populate the resume:

- data/education.json
- data/identity.json
- data/positions.json
- data/projects.json
- data/skills.json

Examples of each are provided below.

## data/education.json

Information about your education. For example:

```
{
    "name": "University of Pennsylvania",
    "degree": "Computer Science",
    "when": "Fall 2010 - Spring 2014"
}
```

## data/identity.json

```
{
    "name": "Ceasar Bautista",
    "address": "Philadelphia, PA",
    "mobile": "(702) 979 4316",
    "email": "cbautista2010@gmail.com",
    "github": "Ceasar"
}
```

## data/positions.json

```
[
    {
        "company": "PennApps Labs",
        "title": "Software Engineer",
        "href": "http://labs.pennapps.com",
        "start": "March 2011",
        "end": "Present",
        "where": "Philadelphia",
        "what": [
            "Open-sourced a lazy Python <a href='http://github.com/pennappslabs/penncoursereview-sdk-python'>wrapper for the Penn Course Review API</a>.",
            "Constructed the <a href='http://penncoursereview.com'>PennCourseReview front-end website</a>.",
            "Constructed the <a href='http://cfa.pennapps.com/'>Penn Common Funding Application</a> which lets students apply for funding for group events online."
        ]
    }, {
        "company": "Lore",
        "title": "Software Engineer, Intern",
        "href": "http://lore.com",
        "start": "May 2012",
        "end": "August 2012",
        "where": "New York City",
        "what": [
            "Worked closely with designers to translate design specs for the user dashboard, 'focus mode' modal, and 'we bar' (chat bar), into working products.",
            "Wrote automated, cloud-based, cross-browser tests to test critical parts of the website.",
            "Integrated Mixpanel analytics to track user behavior."
        ]
    }, {
        "company": "CIS 192 (Python)",
        "title": "Teaching Assistant",
        "href": "http://www.seas.upenn.edu/~cis192/",
        "start": "January 2012",
        "end": "May 2012",
        "where": "Philadelphia",
        "what": [
            "Redesigned and implemented the <a href='http://github.com/CIS192/grader'>grading tool</a> on top of the internals of Python's unittest library.",
            "Designed assignments, covered lectures, assisted students with assignments, and reimplemented submission shell scripts in Python."
        ]
    }
]
```

## data/projects.json

This is a list of the name of Github projects you want to show off. The rest of
the data is populated from the Github API.

```
[
    "staticjinja",
    "pep8fix",
    "regex",
]
```

## data/skills.json

This is a list of skills you have.

```
[
    "Python, Flask, Werkzeug, Django, SQLAlchemy, pytest",
    "HTML, CSS, Javascript, HTTP, IMAP",
    "UNIX, make, git",
    "Unicode"
]
```

## Compilation

My ruby is a little weak, but to compile the sass to css requires
[compass](http://compass-style.org/) (this is because the sass requires
bootstrap-sass which requires compass). Once installed, run `compass watch
static` and it will watch for any changes and update the css accordingly.

# Converting to PDF

To convert the web page to a PDF, the best way I've found is just to print to
PDF (making sure to uncheck headers and footers). A print button is on the
screen version of the resume for convenience.
