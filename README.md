# django-podcast
> A small django app to easily publish podcasts

### Installation
1. Add `podcast` to your `INSTALLED_APPS` in `settings.py`
```python
INSTALLED_APPS = (
    ...
    'podcast',
)
```

2. Add these lines to your URL configuration, `urls.py`
```python
urlpatterns = (
    (r'^podcasts/', include('podcast.urls')),
)
```

### Relevant links
* [RSS 2.0 specification](https://cyber.harvard.edu/rss/rss.html)
* [DjangoAppChecklist](http://djangoappschecklist.com)