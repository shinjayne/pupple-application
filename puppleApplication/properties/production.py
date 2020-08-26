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
            'USER': 'dbmasteruser',
            'PASSWORD': os.environ.get('PUPPLE_MAGIC_CODE', ''),
            'HOST': 'ls-a319742bc22d16b76574c26f3dfa2f21ddd4f938.cphakafsq0ss.ap-northeast-2.rds.amazonaws.com',
            'PORT': 3306,
        }
    }

    DEBUG = False
