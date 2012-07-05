##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, component
from zope.traversing.browser import absoluteURL
from zope.app.pagetemplate import ViewPageTemplateFile

from interfaces import IRSS2Feed


class RSS2Feed(object):
    interface.implements(IRSS2Feed)

    title = u''
    description = u''
    language = None
    date = None
    buildDate = None
    editor = None
    webmaster = None

    template = ViewPageTemplateFile('rss2.pt', content_type='text/xml')

    def __init__(self, context):
        self.context = context

    @property
    def link(self):
        return '%s/'%absoluteURL(self.context, self.request)

    @property
    def contexttitle(self):
        return getattr(self.context, 'title', u'')

    def render(self, request):
        self.request = request
        return self.template()

    def items(self):
        raise NotImplemented('items')


class feedTitle(object):
    """ view class for feed_title """
