from os import getenv
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Settings for static files and media files

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = BASE_DIR / "uploads"

MEDIA_URL = getenv("DJANGO_MEDIA_URL")

# Security settings

SECRET_KEY = getenv("DJANGO_SECRET_KEY")

DEBUG = getenv("DJANGO_DEBUG")

CORS_ALLOWED_ORIGINS = getenv("DJANGO_CORS_ALLOWED_ORIGINS").split(" ")

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS").split(" ")

CORS_ALLOW_CREDENTIALS = getenv("DJANGO_CORS_ALLOW_CREDENTIALS") == "True"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # newly added
    "corsheaders",
    "rest_framework",
    "djoser",
    "users",
    "api",
    "django_extensions",
    "django.contrib.admindocs",
]

# Authentication and Authorization settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("users.authentication.CustomJWTAuthentication",),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

AUTH_COOKIE = getenv("DJANGO_AUTH_COOKIE")
AUTH_COOKIE_ACCESS_MAX_AGE = getenv("DJANGO_AUTH_COOKIE_ACCESS_MAX_AGE")
AUTH_COOKIE_REFRESH_MAX_AGE = getenv("DJANGO_AUTH_COOKIE_REFRESH_MAX_AGE")
AUTH_COOKIE_SECURE = getenv("DJANGO_AUTH_COOKIES_SECURE") == "True"
AUTH_COOKIE_HTTP_ONLY = getenv("DJANGO_AUTH_COOKIES_HTTP_ONLY") == "True"
AUTH_COOKIE_SAME_SITE = getenv("DJANGO_AUTH_COOKIES_SAME_SITE")
AUTH_COOKIE_PATH = getenv("DJANGO_AUTH_COOKIES_PATH")

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "password-reset/{uid}/{token}",
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": False,
    "TOKEN_MODEL": None,
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # newly added
    "corsheaders.middleware.CorsMiddleware",
]

# General settings

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

ROOT_URLCONF = "backend.urls"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = getenv("DJANGO_STATIC_URL")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.UserAccount"
