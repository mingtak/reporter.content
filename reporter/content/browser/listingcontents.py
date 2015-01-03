from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class ListingContents(BrowserView):

    template = ViewPageTemplateFile('templates/listingcontents.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog

        currentUser = api.user.get_current().getId()
        self.brain = catalog({"Creator":currentUser,
                              "Type":["Article", "CustomNews"]},
                             sort_on="created",
                             sort_order="reverse",)
        return self.template()
