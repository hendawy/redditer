
from base import *

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.environ.get(
            'SQLITE_DB', 'db.sqlite3')),
    }
}
