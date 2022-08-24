import os
from os import path

USE_TZ = True

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

PROJECT_DIR = path.abspath(path.join(path.dirname(__file__)))

ROOT_URLCONF = "demo.urls"

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "demo.db"}}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "elasticapm.contrib.django",
    "demo",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # default django middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
            ]
        },
    }
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, "../", "staticfiles")  # noqa

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {
        "": {"handlers": ["console"], "propagate": True, "level": "DEBUG"},
        # 'django': {
        #     'handlers': ['console'],
        #     'propagate': True,
        #     'level': 'WARNING',
        # },
    },
}

TEMPLATE_DEBUG = DEBUG = bool(os.getenv("DJANGO_DEBUG", 0))

# === ELASTIC_APM settings ===

ELASTIC_APM = {
    "SERVICE_URL": os.getenv("ELASTIC_APM_SERVER_URL"),
    "SERVICE_NAME": os.getenv("ELASTIC_APM_SERVICE_NAME"),
    "SECRET_TOKEN": os.getenv("ELASTIC_APM_SECRET_TOKEN"),
    "ENVIRONMENT": os.getenv("ELASTIC_APM_ENVIRONMENT"),
    "DEBUG": True,
}
ELASTIC_APM_ENABLED = all(ELASTIC_APM.values())
