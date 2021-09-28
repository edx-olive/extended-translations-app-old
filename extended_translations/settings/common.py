"""
Settings for translations plugin.
"""

from path import Path


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
