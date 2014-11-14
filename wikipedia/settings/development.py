from wikipedia.settings.defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "django_wikipedia_development",
        'USER': "wikipedia",
        'PASSWORD': "wikipedia"
    }
}

