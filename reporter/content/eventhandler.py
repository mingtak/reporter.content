from plone import api

def objectCreatedEvent(object, event):
    portal = api.portal.get()
    view = api.content.get_view(name='plone', context=portal, request=portal.REQUEST,)
    view.request.response.redirect("/thanksforpost")
