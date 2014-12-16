#-*- coding:utf-8 -*-
from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContent
from reporter.content.eventinfo import IEventInfo
from reporter.content.article import IArticle
from reporter.content.contentlist import IContentList
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# viewlet nameing format: ContentType_Position_ViewletFunction
class EventInfo_IAboveContent_ResponsiveAd(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IEventInfo)
    template = ViewPageTemplateFile('template/responsivead.pt')

    def render(self):
        return self.template()


class EventInfo_IAboveContent_Addthis(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IEventInfo)
    template = ViewPageTemplateFile('template/empty.pt')

    def render(self):
        return self.template()


class EventInfo_IAboveContent_Disqus(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IEventInfo)
    template = ViewPageTemplateFile('template/empty.pt')

    def render(self):
        return self.template()


class Article_IAboveContent_ResponsiveAd(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/responsivead.pt')

    def render(self):
        return self.template()


class Article_IAboveContent_Addthis(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/empty.pt')

    def render(self):
        return self.template()


class Article_IAboveContent_Disqus(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/empty.pt')

    def render(self):
        return self.template()


class ContentList_IAboveContent_ResponsiveAd(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IContentList)
    template = ViewPageTemplateFile('template/responsivead.pt')

    def render(self):
        return self.template()
