"""
App configuration for extended_translations_plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class ExtendedTranslationsPluginConfig(AppConfig):
    """
     Open edX translatable plugin app configuration.
    """
    name = 'extended_translations_plugin'
    verbose_name = ' Open edX translatable plugin app'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'extended_translations_plugin',
                'regex': r'^extended_translations_plugin/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'extended_translations_plugin',
                'regex': r'^extended_translations_plugin/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
