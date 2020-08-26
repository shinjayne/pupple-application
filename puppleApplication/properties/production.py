import os

from puppleApplication.properties.base import BaseProperties


class ProductionProperties(BaseProperties):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'django.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

    ALLOWED_HOSTS = [
        '3.34.90.4',  # EC2 IP
        'pupple-backend-lb-production-912691952.ap-northeast-2.elb.amazonaws.com', # ELB
        'localhost',
        '127.0.0.1',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pupple',
            'USER': 'master',
            'PASSWORD': os.environ.get('PUPPLE_MAGIC_CODE', ''),
            'HOST': 'pupple-db.cxkrqyqhsa8o.ap-northeast-2.rds.amazonaws.com',
            'PORT': 3306,
            'TIME_ZONE': 'Asia/Seoul',
        }
    }

    DEBUG = True
