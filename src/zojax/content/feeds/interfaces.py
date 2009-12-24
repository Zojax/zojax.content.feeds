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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.content.feeds')


class IFeed(interface.Interface):
    """ content feed """

    name = schema.TextLine(
        title = u'Feed name',
        required = True)

    title = schema.TextLine(
        title = u'Feed title',
        required = True)

    description = schema.TextLine(
        title = u'Feed description',
        required = True)

    def render(request):
        """ render feed """


class IRSS2Feed(IFeed):
    """ rss 2.0 feed """

    contexttitle = interface.Attribute('Context Title')
    link = interface.Attribute('RSS Link')
    language = interface.Attribute('RSS Language')
    date = interface.Attribute('RSS pubDate')
    buildDate = interface.Attribute('RSS lastBuildDate')
    editor = interface.Attribute('RSS managingEditor')
    webmaster = interface.Attribute('RSS webMaster')

    def items():
        """ return list of items """
