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

# for addform
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# for i18n
from reporter.content import MessageFactory as _


class IArticle(form.Schema, IImageScaleTraversable):
    """
    Article content type
    """
    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_image",
                      default=u"Please upload lead image, this image will show in cover."),
        required=False,
    )

    text = RichText(
        title=_(u"News content"),
        required=True,
    )


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('addFormForArticle.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('editFormForArticle.pt')


class EditView(DefaultEditView):
    form = EditForm


class Article(Container):
    grok.implements(IArticle)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IArticle)
    grok.require('zope2.View')
    # grok.name('view')
