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
from zope.location import Location
from zope.component import getAdapters, queryAdapter, queryMultiAdapter
from zope.publisher.browser import BrowserPage
from zope.publisher.interfaces import NotFound
from zope.publisher.interfaces.browser import IBrowserPublisher

from interfaces import _, IFeed


class Feeds(Location):
    component.adapts(interface.Interface, interface.Interface)
    interface.implements(IBrowserPublisher)

    __name__ = '@@feeds'
    title = _(u'RSS Feeds')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def __parent__(self):
        return self.context

    def listFeeds(self):
        feeds = []
        for name, feed in getAdapters((self.context,), IFeed):
            feeds.append((feed.title, name, feed))

        feeds.sort()
        return [feed for title, name, feed in feeds]

    def publishTraverse(self, request, name):
        feed = queryAdapter(self.context, IFeed, name=name)
        if feed is not None:
            return FeedView(self, request, feed)

        view = queryMultiAdapter((self, request), name=name)
        if view is not None:
            return view

        raise NotFound(self, name, request)

    def browserDefault(self, request):
        return self, ('index.html',)


class FeedView(BrowserPage):

    def __init__(self, context, request, feed):
        super(FeedView, self).__init__(context, request)

        self.feed = feed

    @property
    def __name__(self):
        return self.feed.name

    def __call__(self):
        return self.feed.render(self.request)
