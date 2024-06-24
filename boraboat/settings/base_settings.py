from corsheaders.defaults import default_headers
from .env import *

SITE_ID = 1
SECRET_KEY = env("SECRET_KEY")

class DEP:
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"

DEPLOYMENT = env("DEPLOYMENT", default=DEP.LOCAL)

DEBUG = False
CSRF_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

DEBUG = False

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]


if DEPLOYMENT == DEP.LOCAL:
    DEBUG = True
    CSRF_COOKIE_SECURE = False

if DEPLOYMENT != DEP.PRODUCTION:
    CORS_ALLOW_ALL_ORIGINS = True
    ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ["*"]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

INSTALLED_APPS = [
    # django libs
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # external libs
    'rest_framework',
    'rest_framework_swagger',
    "corsheaders",  # Добавлено
    # my apps
    'api',
    'users',
    'referal',
    'events',
    'calculation',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Добавлено
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "boraboat.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "boraboat.wsgi.application"
ASGI_APPLICATION = "boraboat.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB", default="local"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("DB_PORT", default=5432),
        "USER": env("POSTGRES_USER", default="user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="password"),
    }
}

if "DATABASE_URL" in os.environ:  # pragma: no cover
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES["default"] = dj_database_url.config()


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


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True



STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = env('EMAIL_BACKEND')
FROM_EMAIL=env('FROM_EMAIL')
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = env('SERVER_EMAIL')
EMAIL_ADMIN = env('EMAIL_ADMIN')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')


CSRF_TRUSTED_ORIGINS = [
   'http:///buraboat-b.prod-it.com', 'https://buraboat.com', 'http://buraboat.com', 'https://buraboat-b.prod-it.com']

# CSRF_TRUSTED_ORIGINS = [
#    'http:///buraboat-b.prod-it.com', 'http://127.0.0.1:8000', 'https://127.0.0.1', 'https://127.0.0.1:3040', 'http://127.0.0.1:3040',
# ]
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS=True

EMAIL_SENDING_ENABLED=os.getenv('EMAIL_SENDING_ENABLED', 'Default-Value')
