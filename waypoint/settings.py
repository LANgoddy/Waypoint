# ---------------------------------------------------------
# WAYPOINT DJANGO PROJECT SETTINGS
# ---------------------------------------------------------

# Import Path so Django can work with project directories.
from pathlib import Path


# ---------------------------------------------------------
# BASE DIRECTORY
# ---------------------------------------------------------

# Build paths inside the project.
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------

# Secret key used by Django.
# This is suitable for our local development project.
SECRET_KEY = "django-insecure-waypoint-development-key"

# Turn debugging on while developing Waypoint locally.
DEBUG = True

# Hosts that are allowed to access the application.
# Empty is fine while DEBUG is True for local development.
ALLOWED_HOSTS = []


# ---------------------------------------------------------
# INSTALLED APPLICATIONS
# ---------------------------------------------------------

INSTALLED_APPS = [

    # Django's built-in applications.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Waypoint trails application.
    "trails",
]


# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------------------------------------------------------
# URL CONFIGURATION
# ---------------------------------------------------------

ROOT_URLCONF = "waypoint.urls"


# ---------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # App templates are stored inside each Django app.
        "DIRS": [],

        # Allow Django to find templates inside installed apps.
        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ---------------------------------------------------------
# WSGI APPLICATION
# ---------------------------------------------------------

WSGI_APPLICATION = "waypoint.wsgi.application"


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

# Use SQLite for the Waypoint project.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ---------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------

# URL used for CSS and other static files.
STATIC_URL = "static/"


# ---------------------------------------------------------
# DEFAULT PRIMARY KEY
# ---------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ---------------------------------------------------------
# WEEK 13 - LOGGING CONFIGURATION
# ---------------------------------------------------------

# Configure logging for the Waypoint application.
LOGGING = {

    # Use Django's logging configuration format.
    "version": 1,

    # Keep Django's existing loggers active.
    "disable_existing_loggers": False,

    # Control how log messages appear.
    "formatters": {

        "simple": {
            "format": "{levelname} {asctime} {name} - {message}",
            "style": "{",
        },
    },

    # Decide where log messages should be displayed.
    "handlers": {

        # Display our messages in the PyCharm terminal.
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },

    # Configure logging specifically for the trails app.
    "loggers": {

        "trails": {

            # Send trails log messages to the terminal.
            "handlers": ["console"],

            # Record INFO messages and anything more serious.
            "level": "INFO",

            # Prevent duplicate messages.
            "propagate": False,
        },
    },
}