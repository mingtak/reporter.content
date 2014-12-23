from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class ContactUs(BrowserView):

    template = ViewPageTemplateFile('templates/thanksforcontactus.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog
        host = self.context.MailHost
        email = request['email']
        if email.strip() == "":
            self.validateEmail = False
            return self.template()
        if not host.validateEmailAddresses(email):
            self.validateEmail = False
            return self.template()
        self.validateEmail = True
        api.portal.get()
        api.portal.send_email(
            recipient="service@mingtak.com.tw",
            sender=request['email'],
            subject="message from reporter",
            body='Email %s \n Message %s' % (request['email'], request['message']),
        )

        return self.template()
