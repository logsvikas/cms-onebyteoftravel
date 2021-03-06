# -*- coding: utf-8 -*-
from cms.api import create_page
from cms.models.pagemodel import Page


class NavextendersFixture(object):
    def create_fixtures(self):
        """
        Tree from fixture:

            page1
                page2
                    page3
            page4
                page5
        """
        defaults = {
            'template': 'nav_playground.html',
            'language': 'en',
        }
        with self.settings(CMS_PERMISSION=False):
            p1 = create_page('page1', published=True, in_navigation=True, **defaults)
            p1.set_as_homepage()
            p4 = create_page('page4', published=True, in_navigation=True, **defaults)
            p1 = Page.objects.get(pk=p1.pk)
            p2 = create_page('page2', published=True, in_navigation=True, parent=p1, **defaults)
            create_page('page3', published=True, in_navigation=True, parent=p2, **defaults)
            p4 = Page.objects.get(pk=p4.pk)
            create_page('page5', published=True, in_navigation=True, parent=p4, **defaults)
