=================================
 Open edX translatable plugin app
=================================

Description
###########

Extends the list of locale path and sets the first locale folder from the current plugin.
This action allows overriding existed translations or add new without
changes in Open edX, and it's dependencies translations in each repository.


Features
########

Override translations for edx-platform and xblocks adding custom translations to django.po, djangojs.po
and by generating .mo and .js files in this app.

Installation
############

Open edX devstack
*****************

- Clone this repo in the src folder of your devstack.
- Open a new Lms/Devstack shell.
- Install the plugin as follows: pip install -e ./src/extended_translations or pip install -e /edx/edxapp/src/extended_translations
- Restart Lms/Studio services.

Usage
#####

- Add new custom translations to django.po and djangojs.po for different languages
- Compile .mo and .js files in LMS/Studio environment
- After installing application in OpenedX environment, translations will be overrided

Contributing
############

Add your contribution policy. (If required)
