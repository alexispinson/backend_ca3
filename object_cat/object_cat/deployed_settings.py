#settings to be deployed on the server
#I will only comment what is different from the development settings


from pathlib import Path
import os

# This 3 lines make sure that https is used 
#-------------------------------------------
SECURE_SSL_REDIRECT = True
SESSION_COOKIE = True
CSRF_COOKIE_SECURE = True
#-------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# here I am going to hide the secret key. I will put it in the .env file which will be hide in the .gitignore file. After that, I will load it using dotenv
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.

SECRET_KEY = str(os.getenv('SECRET_KEY')) # I will have to load the secret key that is in the .env file

# switch debut to false to avoid misconfiguration
DEBUG = False

# change the allowed_hosts (note that I will have to add the domain name of my website when it will be on server)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cat.apps.CatConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'object_cat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'object_cat.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',  
        'PASSWORD': 'password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306', 
    }
}



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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
