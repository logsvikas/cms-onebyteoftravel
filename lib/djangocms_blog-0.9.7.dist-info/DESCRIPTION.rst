==============
djangocms-blog
==============

|Gitter| |PyPiVersion| |PyVersion| |Status| |TestCoverage| |CodeClimate| |License|

django CMS blog application - Support for multilingual posts, placeholders, social network meta tags and configurable apphooks.

Supported Django versions:

* Django 1.8
* Django 1.9
* Django 1.10
* Django 1.11

Supported django CMS versions:

* django CMS 3.2+

.. warning:: Strict dependency on aldryn-search, haystack has been dropped. Install
             them separately to enable full text search support. See `installation docs`_
             for details.

.. warning:: Version 0.8 will be the last one supporting Python 2.6, Python 3.3,
             Django<1.8 and django CMS<3.2.

.. warning:: Starting from version 0.8, date_published is not set anymore
             when creating a post but rather when publishing.
             This does not change the overall behavior, but be warned if you
             expect it to be not null in custom code.

*****************************************
Upgrading cmsplugin-filer from 1.0 to 1.1
*****************************************

Due to changes in cmsplugin-filer/filer which moved ``ThumbnailOption`` model from the
former to the latter, ``djangocms-blog`` must be migrated as well.

Migrating cmsplugin-filer to 1.1 and djangocms-blog up to 0.8.4
===============================================================

If you have djangocms-blog up to 0.8.4 (included) installed or you are upgrading from a previous
djangocms-blog version together with cmsplugin-filer upgrade, you can just apply the migrations::

    pip install cmsplugin-filer==1.1.3 django-filer==1.2.7 djangocms-blog==0.8.4
    python manage.py migrate

Migrating cmsplugin-filer to 1.1 and djangocms-blog 0.8.5+
==========================================================

If you already a djangocms-blog 0.8.5+ up to 0.8.11, upgrade to 0.8.11, then
you have to de-apply some blog migrations when doing the upgrade::

    pip install djangocms-blog==0.8.11
    python manage.py migrate djangocms_blog 0017 ## reverse for these migration is a noop
    pip install cmsplugin-filer==1.1.3 django-filer==1.2.7
    python manage.py migrate

After this step you can upgrade to 0.8.12::

    pip install djangocms-blog==0.8.12

.. note:: de-apply migration **before** upgrading cmsplugin-filer. If running before upgrade, the
          backward migration won't alter anything on the database, and it will just allow the code
          to migrate ``ThumbnailOption`` from cmsplugin-filer to filer

.. note:: If you upgrade in a Django 1.10 environment, be sure to upgrade both packages
          at the same time to allow correct migration dependencies to be evaluated.

Installing djangocms-blog in an existing project with Django 1.10
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If your project has cmsplugin-filer 1.1+ already installed and it uses Django 1.10,
install djangocms-blog 0.8.12 (and above)::

    pip install djangocms-blog==0.8.12

********
Features
********

* Placeholder content editing
* Frontend editing using django CMS 3.x frontend editor
* Multilingual support using django-parler
* Twitter cards, Open Graph and Google+ snippets meta tags
* Optional simpler TextField-based content editing
* Multisite (posts can be visible in one or more Django sites on the same project)
* Per-Apphook configuration
* Configurable permalinks
* Configurable django CMS menu
* Per-Apphook templates set
* Auto Apphook setup
* Django sitemap framework
* django CMS 3.2+ Wizard
* Haystack index
* Desktop notifications
* Liveblog

*****************************
Known djangocms-blog websites
*****************************

See DjangoPackages for an updated list https://www.djangopackages.com/packages/p/djangocms-blog/


.. _installation docs: http://djangocms-blog.readthedocs.io/en/latest/installation.html



.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-blog
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-blog
    :alt: Python versions

.. |Status| image:: https://img.shields.io/travis/nephila/djangocms-blog.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-blog
    :alt: Latest Travis CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-blog/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-blog?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-blog.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-blog/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-blog/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-blog
   :alt: Code Climate




=======
History
=======

******************
0.9.7 (2018-05-05)
******************

* Fixed subtitle field not added to the admin

******************
0.9.6 (2018-05-02)
******************

* Fixed string representation when model has no language
* Added subtitle field

******************
0.9.5 (2018-04-07)
******************

* Fixed jquery path in Django 1.9+"Fix jquery path in Django 1.9+
* Added configurable blog abstract/text CKEditor

******************
0.9.4 (2018-03-24)
******************

* Fixed migration error from 0.8 to 0.9

******************
0.9.3 (2018-03-12)
******************

* Added dependency on lxml used in feeds
* Fixed warning on django CMS 3.5
* Fixed wizard in Django 1.11
* Updated translations

******************
0.9.2 (2018-02-27)
******************

* Fixed missing migration

******************
0.9.1 (2018-02-22)
******************

* Added Django 1.11 support

******************
0.9.0 (2018-02-20)
******************

* Added support for django CMS 3.4, 3.5
* Dropped support for Django<1.8, django CMS<3.2.
* Added liveblog application.
* Refactored plugin filters: by default only data for current site are now shown.
* Added global and per site posts count to BlogCategory.
* Added option to hide empty categories from menu.
* Added standalone documentation at https://djangocms-blog.readthedocs.io.
* Enabled cached version of BlogLatestEntriesPlugin.
* Added plugins templateset.
* Improved category admin to avoid circular relationships.
* Dropped strict dependency on aldryn-search, haystack. Install separately for search support.
* Improved admin filtering.
* Added featured date to post.
* Fixed issue with urls in sitemap if apphook is not published
* Moved template to easy_thumbnails_tags template tag. Require easy_thumbnails >= 2.4.1
* Made HTML description and title fields length configurable
* Added meta representation for CategoryEntriesView
* Generated valid slug in wizard if the given one is taken
* Fixed error in category filtering when loading the for via POST
* Returned 404 in AuthorEntriesView if author does not exists
* Returned 404 in CategoryEntriesView if category does not exists
* Generate valid slug in wizard if the given one is taken
* Limit categories / related in forms only to current lan

*******************
0.8.13 (2017-07-25)
*******************

* Dropped python 2.6 compatibility
* Fixed exceptions in __str__
* Fixed issue with duplicated categories in menu

*******************
0.8.12 (2017-03-11)
*******************

* Fixed migrations on Django 1.10

*******************
0.8.11 (2017-03-04)
*******************

* Fixed support for aldryn-apphooks-config 0.3.1

*******************
0.8.10 (2017-01-02)
*******************

* Fix error in get_absolute_url

******************
0.8.9 (2016-10-25)
******************

* Optimized querysets
* Fixed slug generation in wizard

******************
0.8.8 (2016-09-04)
******************

* Fixed issue with one migration
* Improved support for django CMS 3.4

******************
0.8.7 (2016-08-25)
******************

* Added support for django CMS 3.4
* Fixed issue with multisite support

******************
0.8.6 (2016-08-03)
******************

* Set the correct language during indexing

******************
0.8.5 (2016-06-26)
******************

* Fixed issues with ThumbnailOption migration under mysql.

******************
0.8.4 (2016-06-22)
******************

* Fixed issues with cmsplugin-filer 1.1.

******************
0.8.3 (2016-06-21)
******************

* Stricter filer dependency versioning.

******************
0.8.2 (2016-06-12)
******************

* Aldryn-only release. No code changes

******************
0.8.1 (2016-06-11)
******************

* Aldryn-only release. No code changes

******************
0.8.0 (2016-06-05)
******************

* Added django-knocker integration
* Changed the default value of date_published to null
* Cleared menu cache when changing menu layout in apphook config
* Fixed error with wizard multiple registration
* Made django CMS 3.2 the default version
* Fixed error with on_site filter
* Removed meta-mixin compatibility code
* Changed slug size to 255 chars
* Fixed pagination setting in list views
* Added API to set default sites if user has permission only for a subset of sites
* Added Aldryn integration

******************
0.7.0 (2016-03-19)
******************

* Make categories non required
* Fix tests with parler>=1.6
* Use all_languages_column to admin
* Add publish button
* Fix issues in migrations. Thanks @skirsdeda
* Fix selecting current menu item according to menu layout
* Fix some issues with haystack indexes
* Add support for moved ThumbnailOption
* Fix Django 1.9 issues
* Fix copy relations method in plugins
* Mitigate issue when apphook config can't be retrieved
* Mitigate issue when wizard double registration is triggered

******************
0.6.3 (2015-12-22)
******************

* Add BLOG_ADMIN_POST_FIELDSET_FILTER to filter admin fieldsets
* Ensure correct creation of full URL for canonical urls
* Move constants to settings
* Fix error when no config is found

******************
0.6.2 (2015-11-16)
******************

* Add app_config field to BlogLatestEntriesPlugin
* Fix __str__ plugins method
* Fix bug when selecting plugins template

******************
0.6.1 (2015-10-31)
******************

* Improve toolbar: add all languages for each post
* Improve toolbar: add per-apphook configurable changefreq, priority

******************
0.6.0 (2015-10-30)
******************

* Add support for django CMS 3.2 Wizard
* Add support for Apphook Config
* Add Haystack support
* Improved support for meta tags
* Improved admin
* LatestPostsPlugin tags field has been changed to a plain TaggableManager field.
  A migration is in place to move the data, but backup your data first.

******************
0.5.0 (2015-08-09)
******************

* Add support for Django 1.8
* Drop dependency on Django select2
* Code cleanups
* Enforce flake8 / isort checks
* Add categories menu
* Add option to disable the abstract

******************
0.4.0 (2015-03-22)
******************

* Fix Django 1.7 issues
* Fix dependencies on python 3 when using wheel packages
* Drop Django 1.5 support
* Fix various templates issues
* UX fixes in the admin

******************
0.3.1 (2015-01-07)
******************

* Fix page_name in template
* Set cascade to set null for post image and thumbnail options

******************
0.3.0 (2015-01-04)
******************

* Multisite support
* Configurable default author support
* Refactored settings
* Fix multilanguage issues
* Fix SEO fields length
* Post absolute url is generated from the title in any language if current is
  not available
* If djangocms-page-meta and djangocms-page-tags are installed, the relevant
  toolbar items are removed from the toolbar in the post detail view to avoid
  confusings page meta / tags with post ones
* Plugin API changed to filter out posts according to the request.
* Django 1.7 support
* Python 3.3 and 3.4 support

******************
0.2.0 (2014-09-24)
******************

* **INCOMPATIBLE CHANGE**: view names changed!
* Based on django parler 1.0
* Toolbar items contextual to the current page
* Add support for canonical URLs
* Add transifex support
* Add social tags via django-meta-mixin
* Per-post or site-wide comments enabling
* Simpler TextField-based content editing for simpler blogs
* Add support for custom user models

******************
0.1.0 (2014-03-06)
******************

* First experimental release


