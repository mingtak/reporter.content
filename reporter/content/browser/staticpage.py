from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ThanksForPost(BrowserView):

    template = ViewPageTemplateFile('templates/thanksforpost.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog
        return self.template()
