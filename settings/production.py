from .base import *
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://www.mystudynotebook.com',
    'http://mystudynotebook.com',
    'www.mystudynotebook.com',
    'mystudynotebook.com',
    '139.162.45.141'
]

# logging settings for production. print to console.save to file
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'production_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/html/mystudynotebook.com/log/django.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['production_file'],
            'level': 'INFO',
        },
    },
}
