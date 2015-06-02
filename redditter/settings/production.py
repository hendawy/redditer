
from base import *

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import dj_database_url
DATABASES = {'default': dj_database_url.config(
    default=os.environ.get('DATABASE_URL'))}
