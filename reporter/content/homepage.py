from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone import api

# for add/edit form
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# i18n
from reporter.content import MessageFactory as _


class IHomePage(form.Schema, IImageScaleTraversable):
    """
    Home page content type
    """


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class HomePage(Container):
    grok.implements(IHomePage)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')

    def slideSetup(self):
        registry = "reporter.content.configlet.homepagelayoutsetting.IHomepageLayoutSetting.slideSetup"
        value = api.portal.get_registry_record(registry)
        return value

    def eventSetup(self):
        registry = "reporter.content.configlet.homepagelayoutsetting.IHomepageLayoutSetting.eventSetup"
        value = api.portal.get_registry_record(registry)
        return value

    def competitionSetup(self):
        registry = "reporter.content.configlet.homepagelayoutsetting.IHomepageLayoutSetting.competitionSetup"
        value = api.portal.get_registry_record(registry)
        return value

    def articleSetup(self):
        registry = "reporter.content.configlet.homepagelayoutsetting.IHomepageLayoutSetting.articleSetup"
        value = api.portal.get_registry_record(registry)
        return value

    def customNewsSetup(self):
        registry = "reporter.content.configlet.homepagelayoutsetting.IHomepageLayoutSetting.customNewsSetup"
        value = api.portal.get_registry_record(registry)
        return value

    def catalog(self):
        return self.context.portal_catalog
