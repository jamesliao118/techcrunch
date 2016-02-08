import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Randall Degges', 'r@rdegges.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'techcrunch.db',
    }
}

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'techcrunch.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/'

# URL of the login page.
LOGIN_URL = '/login/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'somerandomnumbers'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'techcrunch.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'portal',
)