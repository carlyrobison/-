"""
Settings for shower-pomelo-bot
"""

from distutils.util import strtobool

import logging
import os

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "shower-pomelo-bot.herokuapp.com",
]

# This should be turned on in production to redirect HTTP to HTTPS
# The development web server doesn't support HTTPS, however, so do not
# turn this on in dev.
SECURE_SSL_REDIRECT = bool(strtobool(os.environ.get("SECURE_SSL_REDIRECT", "False")))

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = "/static/"
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "smallboard/static"),
    # os.path.join(BASE_DIR, "hunts/static"),
]

# Discord API. See
# https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-
DISCORD_API_TOKEN = os.environ.get("DISCORD_API_TOKEN", None)

# Discord server ID.

# Category (folder) to contain generated channels.
try:
    DISCORD_PUZZLE_CATEGORY = os.environ["DISCORD_PUZZLE_CATEGORY"]
    DISCORD_ARCHIVE_CATEGORY = os.environ["DISCORD_ARCHIVE_CATEGORY"]
except KeyError as e:
    logger.warn(
        f"No {e.args[0]} found in environment. Automatic category creation disabled."
    )


# Google Drive API
try:
    GOOGLE_API_AUTHN_INFO = {
        "type": "service_account",
        "project_id": os.environ["GOOGLE_API_PROJECT_ID"],
        "private_key_id": os.environ["GOOGLE_API_PRIVATE_KEY_ID"],
        "private_key": os.environ["GOOGLE_API_PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": os.environ["GOOGLE_API_CLIENT_EMAIL"],
        "client_id": os.environ["GOOGLE_API_CLIENT_ID"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ["GOOGLE_API_X509_CERT_URL"],
    }
    GOOGLE_DRIVE_PERMISSIONS_SCOPES = ["https://www.googleapis.com/auth/drive"]
    GOOGLE_DRIVE_HUNT_FOLDER_ID = os.environ["GOOGLE_DRIVE_HUNT_FOLDER_ID"]
    GOOGLE_DRIVE_SOLVED_FOLDER_ID = os.environ["GOOGLE_DRIVE_SOLVED_FOLDER_ID"]
    GOOGLE_SHEETS_TEMPLATE_FILE_ID = os.environ["GOOGLE_SHEETS_TEMPLATE_FILE_ID"]
except KeyError as e:
    GOOGLE_API_AUTHN_INFO = None
    logger.warn(
        f"No {e.args[0]} found in environment. Automatic sheets creation disabled."
    )


AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
]

# Chat app settings.

if not "DISCORD_API_TOKEN" in os.environ:
    logger.warn(
        "No Discord API token found in environment. Automatic Discord channel creation disabled."
    )
