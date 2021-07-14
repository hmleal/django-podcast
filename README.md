# django-podcast

> A small django app to easily publish podcasts

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/hmleal/django-podcast.svg?branch=master)](https://travis-ci.org/hmleal/django-podcast)

## Requirements

* Python (3.8, 3.9)
* Django (3.2)

## Installation

Install using `pip` ...

    pip install django-podcast

Add `'podcast'` to your `INSTALLED_APPS` setting

    INSTALLED_APPS = [
        ...
        'podcast',
    ]

Add these lines to your URL configuration, `urls.py`

    urlpatterns = (
        path('podcasts/', include('podcast.urls')),
    )

And finally migrate your database

    python manage.py migrate podcast

### Relevant links

- [RSS 2.0 specification](https://cyber.harvard.edu/rss/rss.html)
- [DjangoAppChecklist](http://djangoappschecklist.com)
- [Feed NerdCast](https://jovemnerd.com.br/feed-nerdcast)
