"""
Plugin configuration for integration application to the edx-platform.
"""

from django.apps import AppConfig

from openedx.core.djangoapps.plugins.constants import (
    PluginSettings,
    PluginURLs,
    ProjectType,
    SettingsType,
)


class TranslationsPluginConfig(AppConfig):
    name = 'extended_translations'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: u'user_document',
                PluginURLs.REGEX: r'user/document/',
                PluginURLs.RELATIVE_PATH: u'urls',

            },
            ProjectType.CMS: {
                PluginURLs.NAMESPACE: u'user_document',
                PluginURLs.REGEX: r'user/document/',
                PluginURLs.RELATIVE_PATH: u'urls',

            }
        },

        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        }
    }
