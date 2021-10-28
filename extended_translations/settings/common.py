"""
Common Django settings for extended_translations project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from path import Path

from __future__ import unicode_literals

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'


# Application definition

INSTALLED_APPS = []

ROOT_URLCONF = 'extended_translations.urls'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True

def _patched_make_locale_paths(settings):
    """
    Function witch returns patched locale paths.

    Extends the list of locale path and sets the first locale folder from the current plugin.
    This action allows overriding existed translations or add new without
    changing Open edX, and it's dependencies translations in each repository.
    """

    locale_paths = [
        Path(__file__).parent.parent + "/conf/locale",
        settings.REPO_ROOT + '/conf/locale'  # edx-platform/conf/locale/
    ]

    if settings.ENABLE_COMPREHENSIVE_THEMING:
        # Add locale paths to settings for comprehensive theming.
        for locale_path in settings.COMPREHENSIVE_THEME_LOCALE_PATHS:
            locale_paths += (Path(locale_path),)

    return locale_paths


def plugin_settings(settings):
    """
    Updates necessary project settings.
    """
    settings.LOCALE_PATHS = _patched_make_locale_paths
    settings.STATICI18N_ROOT = Path(__file__).parent.parent + "/static"
    settings.STATICFILES_DIRS.insert(0, Path(__file__).parent.parent + "/static")
