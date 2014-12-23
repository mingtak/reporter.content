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

# for add/edit form
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# i18n
from reporter.content import MessageFactory as _


# Interface class; used to define content-type schema.

class IContentList(form.Schema, IImageScaleTraversable):
    """
    Content lists' content type
    """
    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_image",
                      default=u"Please upload lead image, this image will show in cover."),
        required=True,
    )


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class ContentList(Container):
    grok.implements(IContentList)


class ViewForEventInfo(grok.View):

    grok.context(IContentList)
    grok.require('zope2.View')
    grok.name('view for eventinfo')
    # Add view methods here


class ViewForCustomNews(grok.View):

    grok.context(IContentList)
    grok.require('zope2.View')
    grok.name('view for customnews')
    # Add view methods here


class ViewForArticle(grok.View):

    grok.context(IContentList)
    grok.require('zope2.View')
    grok.name('view for article')
    # Add view methods here


class ViewForCompetition(grok.View):

    grok.context(IContentList)
    grok.require('zope2.View')
    grok.name('view for competition')
    # Add view methods here


class ViewForNone(grok.View):

    grok.context(IContentList)
    grok.require('zope2.View')
    grok.name('view for none')
    # Add view methods here
