import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

__all__ = []


def load_bool(name, default):
    env_value = os.getenv(name, str(default)).lower()
    return env_value in ("true", "yes", "1", "y", "t")


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fake")

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost",
).split(",")

INTERNAL_IPS = [
    "concovpr.beget.tech",
    "127.0.0.1",
    "lcoalhost",
]

DEBUG = load_bool("DJANGO_DEBUG", True)

DEFAULT_USER_IS_ACTIVE = True

MAX_ATTEMPTS_AUTH = ...

EMAIL_HOST = "beget.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "klevoemestechko@klevoemestechko.ru"
EMAIL_PASSWORD = "1Ds8oxCf6Qqj"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


INSTALLED_APPS = [
    # джанго
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # стороние модули
    "sorl.thumbnail",
    "django_cleanup.apps.CleanupConfig",
    "ckeditor",
    "ckeditor_uploader",
    # "cities_light",
    "rest_framework",
    "corsheaders",
    "social_django",
    # наше
    "users.apps.UsersConfig",
    "catalog.apps.CatalogConfig",
    "moderation.apps.ModerationConfig",
    "rating.apps.RatingConfig",
    "homepage.apps.HomepageConfig",
    "map.apps.MapConfig",
]

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "OnTheHook.urls"

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
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "OnTheHook.wsgi.application"

AUTHENTICATION_BACKENDS = [
    "OnTheHook.backends.ModifyLogin",
    "social_core.backends.vk.VKOAuth2",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
CORS_ORIGIN_WHITELIST = ("http://localhost:8000",)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_"
            "validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
}

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/auth/login/"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CITIES_LIGHT_TRANSLATION_LANGUAGES = ["ru"]
# CITIES_LIGHT_INCLUDE_COUNTRIES = ["RU"]
# CITIES_LIGHT_INCLUDE_CITY_TYPES = [
#     "PPL",
#     "PPLA",
#     "PPLA2",
#     "PPLA3",
#     "PPLA4",
#     "PPLC",
#     "PPLF",
#     "PPLG",
#     "PPLL",
#     "PPLR",
#     "PPLS",
#     "STLMT",
# ]

CKEDITOR_JQUERY_URL = (
    "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"
)
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {
                "name": "editing",
                "items": ["Find", "Replace", "-", "SelectAll"],
            },
            {"name": "styles", "items": ["Styles"]},
        ],
        "height": 500,
        "width": 600,
        "extraPlugins": "codesnippet",
        "toolbarLocation": "bottom",
        "bodyClass": "text-center",
    },
}

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_VK_OAUTH2_KEY = "51818085"
SOCIAL_AUTH_VK_OAUTH2_SECRET = "orkcjbrxdOFh01Wn1IBK"

YANDEX_OAUTH2_CLIENT_KEY = "df2b81aa8dba4561bd3e816345e89aa3" #пока не работает
YANDEX_OAUTH2_CLIENT_SECRET = "d638dbc2967d4e5da8870228de159b4e" #пока не работает

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email"]
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
]
