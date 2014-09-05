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
directly in the HTML. Instead, data is stored inside of `data/resume.json` and
embedded using Javascript and Jinja2. An example `resume.json` appears below:

```
{
    "identity": {
        "name": "John Doe",
        "address": "123 Baker Lane",
        "mobile": "123-456-7890",
        "email": "john@example.com",
        "github": "Ceasar"
    },
    "education": {
        "name": "Stanford University",
        "degree": "BSE in Computer Science",
        "when": "Fall 2010 - Spring 2014",
        "what": "Coursework: Operating Systems, Algorithms, Databases, AI, UNIX"
    },
    "positions": [
        {
            "company": "Clara Labs",
            "title": "Software Engineer",
            "href": "http://claralabs.com",
            "start": "May 2014",
            "end": "Present",
            "where": "San Francisco, CA"
        }, {
            "company": "Facebook",
            "title": "Software Engineer Intern",
            "href": "http://facebook.com",
            "start": "May 2013",
            "end": "July 2013",
            "where": "Menlo Park, CA",
            "what": [
                "Optimized Daily Active Users (DAU) by A/B testing the 'People You May Know' notifications and friend activity notifications sent to stale users.",
                "Overhauled legacy code, increased test coverage, and documented tools."
            ]
        }, {
            "company": "Penn Labs",
            "title": "Software Engineer",
            "href": "http://pennlabs.org/",
            "start": "March 2011",
            "end": "May 2014",
            "where": "Philadelphia, PA",
            "what": [
                "Significantly contributed to <a href='http://eventsatpenn.com/'>Events@Penn</a> using Meteor.js.",
                "Implemented and open-sourced the <a href='http://github.com/pennappslabs/penncoursereview-sdk-python'>Python SDK for the Penn Course Review API</a>.",
                "Implemented the <a href='http://penncoursereview.com'>PennCourseReview</a> client using Django."
            ]
        }, {
            "company": "Lore",
            "title": "Software Engineer, Intern",
            "href": "http://lore.com",
            "start": "May 2012",
            "end": "August 2012",
            "where": "New York City",
            "what": [
                "Implemented multiple pages, including the user dashboard, 'focus mode' modal, and chat bar using Coffeescript and Sass.",
                "Tested critical end-to-end functionality (e.g. logging in, registering) with Selenium.",
                "Tracked user behavior across the site with Mixpanel."
            ]
        }
    ],
    "projects": [
        "twosheds",
        "staticjinja",
        "Encyclopedia",
        "LisPy",
        "regex"
    ],
    "skills": [
    ]
}
```

You should edit this to contain your own data.

## Compilation

My ruby is a little weak, but to compile the sass to css requires
[compass](http://compass-style.org/) (this is because the sass requires
bootstrap-sass which requires compass). Once installed, run `compass watch
static` and it will watch for any changes and update the css accordingly.

# Converting to PDF

To convert the web page to a PDF, the best way I've found is just to print to
PDF (making sure to uncheck headers and footers). A print button is on the
screen version of the resume for convenience.
