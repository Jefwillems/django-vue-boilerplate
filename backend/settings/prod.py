import dj_database_url
from .dev import *

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

DEBUG = bool(os.getenv('DJANGO_DEBUG_MODE', ''))

# TODO: Set to host domain
ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}
