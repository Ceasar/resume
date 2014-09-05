# Overview

An attempt to make a modular resume that is easy to maintain. You can find an
example [here](http://ceasarbautista.com/resume/).

## Features

- Information about your Github projects, such as fork and stars, are included
  as part of your projects so viewers can get of sense of their gravity at a
  glance.
- A "Download" button is included in the screen version for easily generating
  PDFs
- A bibliographic section containing the date accessed and the URL is included
  to ensure interviewers never use an outdated version of your resume (at least
  without knowing it)
- Data is separated from presentation for portability
- Fluid layout for viewing on any device

# Quickstart

To generate the resume, simply run:

```
make index.html
```

This will generate a file `index.html`, an HTML version of your resume, which
is compatible with [Github Pages](https://pages.github.com/).

This may require you to install [Compass](http://compass-style.org/) .

## Data

The resume is meant to be completely modular, so no personal data is embedded
directly in the HTML. Instead, data is stored inside of `data/resume.json` and
embedded using Javascript and Jinja2. An example `resume.json` appears below:

```
{
    "identity": {
        "name": "Ceasar Bautista",
        "address": "275 Capp St, San Franciso, CA, 94110",
        "mobile": "702-979-4316",
        "email": "cbautista2010@gmail.com",
        "github": "Ceasar"
    },
    "education": {
        "name": "University of Pennsylvania",
        "degree": "Computer Science",
        "when": "Fall 2010 - Spring 2014"
    },
    "positions": [
        {
            "company": "Clara Labs",
            "title": "Software Engineer",
            "href": "http://claralabs.com",
            "start": "May 2014",
            "end": "September 2014",
            "where": "San Francisco, CA",
            "what": [
                "Built the Clara REST API, including frameworks to automatically generate and test endpoints, using Flask, SQLAlchemy, and pytest."
            ]
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
        "Python, Flask, Werkzeug, Django, SQLAlchemy, pytest",
        "HTTP, HTML, CSS, Javascript, IMAP",
        "UNIX, Git, Make",
        "Unicode"
    ]
}
```

You should edit this to contain your own information. Note that `projects` is
an array containing the names of the Github projects you want to show (the
actual information is taken from the [Github
API](https://developer.github.com/v3/).
