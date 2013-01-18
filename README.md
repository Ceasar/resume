# Overview

Modular resume.

## Features

- Fluid layout
- Print button in screen version
- Dynamic access and update date
- Data separated from html

# Installation

`pip install -r requirements.txt`

# Quickstart

## Data

The resume is meant to be completely modular. Consequently, personal data is not embedded directly in the HTML. To get around this, data is stored inside of `data/` and embedded using jinja.

The following files are necessary for the resume to work.

- data/identity.json
- data/languages.json
- data/positions.json
- data/projects.json
- data/technologies.json

Examples of each are provided below.

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

## data/languages.json

```
[
    {"name":"Python"},
    {"name":"PHP"}
]
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

```
[
    {
        "name": "staticjinja",
        "what": "Effortlessly deploy static sites.",
        "when": "Fall 2012",
        "href": "https://github.com/Ceasar/staticjinja"
    }, {
        "name": "pep8fix",
        "what": "Correct Python files that don't adhere to PEP8.",
        "when": "Ongoing",
        "href": "https://github.com/Ceasar/pep8fix"
    }, {
        "name": "regex",
        "what": "Haskell regular expression matcher.",
        "when": "Spring 2012",
        "href": "https://github.com/Ceasar/regex"
    }
]
```

## data/technologies.json

```
[
    {"name":"Django"},
    {"name":"HTML/CSS"},
    {"name":"SQL"},
    {"name":"Unix/Git"}

]
```

## Compilation

To compile the templates into the resume, run `python build.py`. This will automatically watch the templates for changes and rebuild the resume on change.

My ruby is a little weak, but to compile the sass to css requires [compass](http://compass-style.org/) (this is because the sass requires bootstrap-sass which requires compass). Once installed, run `compass watch static` and it will watch for any changes and update the css accordingly.

# Converting to PDF

To convert the web page to a PDF, the best way I've found is just to print to PDF (making sure to uncheck headers and footers). A print button is on the screen version of the resume for convenience.
