"""
Django settings for eduaulas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DIR_APP = os.path.join(BASE_DIR,'eduaulas')
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%v*rncfr(ck(1ofvb&(#^cx3xj&p)u7xj^=^g6r_n*5n3^vm_7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
    
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

#CSRF_COOKIE_DOMAIN = '127.0.0.1:8080'


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # 'south', 
    'classroom',
    'teacher',
    'exercise',
    'location',
    'dashboard',
    'student',
    'person',    
    'configurations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eduaulas.urls'

WSGI_APPLICATION = 'eduaulas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eduaulas_db',
        'USER': 'eduaulas_root',
        'PASSWORD': 'eduaulas',
        'HOST': 'eduaulas-db.cnynwpmxidse.us-east-1.rds.amazonaws.com',
        'PORT': '3306',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-UY'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = '/srv/www/eduaulas/media/'
MEDIA_URL = 'http://54.243.196.72/'
STATIC_URL = '/'
STATIC_ROOT = '/srv/www/eduaulas/static/'

EDUAULAS_DIR="/srv/eduaulas/media/eduaulas"
EDUAULAS_GIT="/srv/eduaulas/eduaulas-git"

FILEBROWSER_MEDIA_ROOT="/srv/eduaulas/media"
FILEBROWSER_DIRECTORY="cuasimodo/assets"

GRAPPELLI_ADMIN_TITLE = "ADMINISTRADOR DE EDUAULAS"


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'eduaulas.common.template_base',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
)
TEMPLATE_LOADERS = (
   'django.template.loaders.filesystem.Loader',
   'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(DIR_APP,'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = (
     os.path.join(DIR_APP,'static'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'braulio.deleon@editorialedu.com'
EMAIL_HOST_PASSWORD = 'R31S189matilda'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'braulio.deleon@editorialedu.com'
SERVER_EMAIL = 'braulio.deleon@editorialedu.com'