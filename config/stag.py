import env


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.DB_NAME,
        'USER': env.DB_USER,
        'PASSWORD': env.PASSWORD,
        'HOST': env.DB_HOST,
        'PORT': env.DB_PORT
    }
}
