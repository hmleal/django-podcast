SECRET_KEY = 'fake-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = ('podcast', 'tests')