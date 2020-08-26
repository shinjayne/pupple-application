import os

from puppleApplication.properties.base import BaseProperties


class ProductionProperties(BaseProperties):

    ALLOWED_HOSTS = [
        '3.35.82.232',  # Lightsail Elastic IP
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
        }
    }

    DEBUG = False
