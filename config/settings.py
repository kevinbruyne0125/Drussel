"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from environs import Env


# Setup environment:
env = Env()
env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

# Note - it doesn't appear that the test server supports IPv6
ALLOWED_HOSTS = ['developernexus.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # Django built-ins:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Used by WhiteNoise to manage static files:
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # Used by Django-AllAuth:
    'django.contrib.sites',
    # For human/naturaltime:
    'django.contrib.humanize',

    # 3rd party debugging:
    # 'debug_toolbar',
    # Insert conditionally if DEBUG True

    # 3rd party:
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

    # Local apps:
    'accounts',
    'paths',
    'posts',
    'pages',
]

# Django Debug Toolbar:
if DEBUG:
    target_index = INSTALLED_APPS.index('crispy_forms')
    INSTALLED_APPS.insert(target_index, 'debug_toolbar')


MIDDLEWARE = [
    # 3rd party debugging:
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Insert conditionally if DEBUG True

    # Default:
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Used by Whitenoise:
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Django Debug Toolbar:
if DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.dj_db_url('DATABASE_URL',
    default='sqlite:///db.sqlite3')
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Default - change to my time zone:
# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# URL used to reference static assets (files):
STATIC_URL = '/static/'

# Location of static files directory for local development:
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)

# Location of static files in production (must be distinct name):
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

# How to look for static file directories:
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Used by Whitenoise:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Custom User Model:
AUTH_USER_MODEL = 'accounts.CustomUser'


# Redirect defaults
LOGIN_REDIRECT_URL = 'post_list'
LOGOUT_REDIRECT_URL = 'post_list'


# Django Crispy Forms:
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Django All Auth Config:
SITE_ID = 1

# Authentication:
AUTHENTICATION_BACKENDS = (
    # Django default:
    'django.contrib.auth.backends.ModelBackend',

    # Addition for Django All Auth:
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Django All Auth Settings:

# Change to allow E-mail only registration:
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Change to allow E-mail only registration:
ACCOUNT_EMAIL_REQUIRED = True
# To disable E-mail verification, can also set to 'mandatory':
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# Overrides LOGOUT_REDIRECT_URL:
ACCOUNT_LOGOUT_REDIRECT = 'post_list'
# Default is None which asks user if they want to be remembered:
ACCOUNT_SESSION_REMEMBER = True
# Default is True:
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# Change to allow E-mail only registration:
ACCOUNT_UNIQUE_EMAIL = True
# Default is True, change to False to allow E-mail only registration:
ACCOUNT_USERNAME_REQUIRED = False


# E-mail Settings:
#
if DEBUG:
    # Use the console instead of a SMTP server/relay:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Use a SMTP server:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# EMAIL_BACKEND = env.str('DJANGO_EMAIL_BACKEND')
#
ADMIN_EMAIL = env.str('DJANGO_ADMIN_EMAIL')
# Make sure this account/provider email differ from superuser email or weird errors will result!
DEFAULT_FROM_EMAIL = env.str('DJANGO_DEFAULT_FROM_EMAIL')
#
EMAIL_HOST = env.str('DJANGO_EMAIL_HOST')
EMAIL_HOST_USER = env.str('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_PORT = env.int('DJANGO_EMAIL_PORT')
EMAIL_USE_TLS = env.bool('DJANGO_EMAIL_USE_TLS')


# Django Debug Toolbar:
if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

# Django Debug Toolbar Notes:
#
# For Windows:
# If, "get-itemproperty -path 'Registry::HKCR\.js\' -name 'Content Type'"
# shows 'Content Type' = 'text/plain', you must change it as follows:
# "set-itemproperty -path 'Registry::HKCR\.js\' -name 'Content Type' -Value 'text/javascript'"
# If you change this, you must quit all browser instances and then re-launch the site


# Secure Deployment settings:
if not DEBUG:
    # Need to experiment and site/domain compatible with HSTS:
    SECURE_HSTS_SECONDS = 3600
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
