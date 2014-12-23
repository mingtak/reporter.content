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

# index and metadata
from plone.indexer import indexer
from collective import dexteritytextindexer

# i18n
from reporter.content import MessageFactory as _


@grok.provider(IContextSourceBinder)
def eventCategory(context):
    category = [
        _(u"Arts and Humanities"),
        _(u"Natural science"),
        _(u"Local"),
        _(u"Celebration"),
        _(u"Experience tour"),
        _(u"Other categories"),
    ]
    terms = []
    for item in category:
        terms.append(SimpleVocabulary.createTerm(item, item, item))
    return SimpleVocabulary(terms)


class IEventInfo(form.Schema, IImageScaleTraversable):
    """
    Event information content type
    """
    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_eventinfo_image",
                      default=u"Please upload event cover image, if have."),
        required=False,
    )

    bannerImage = NamedBlobImage(
        title=_(u"Banner image"),
        description=_(u"help_eventinfo_bannerImage",
                      default=u"Please upload event promotion image, if have."),
        required=False,
    )

    eventCategory = schema.Choice(
        title=_(u"Event category"),
        source=eventCategory,
        required=True,
    )

    noticeUrl = schema.URI(
        title=_(u"Notice URL"),
        description=_(u"help_notice_url",
                      default=u"Please upload notice url."),
        required=True,
    )

    signUpFrom = schema.Date(
        title=_(u"Sign up start date"),
        description=_(u"help_signUPFrom",
                      default=u"Sign up from date, if have."),
        required=False,
    )

    signUpEnd = schema.Date(
        title=_(u"Sign up end date"),
        description=_(u"help_signUPEnd",
                      default=u"Sign up end date, if have."),
        required=False,
    )

    happenDate = schema.Date(
        title=_(u"Event date"),
        description=_(u"help_eventinfo_Date",
                      default=u"Event happen date, if have."),
        required=False,
    )

    dexteritytextindexer.searchable('text')
    text = RichText(
        title=_(u"Notice content"),
        description=_(u"help_notice_text",
                      default=u"We will comfirm this notice, then publish it, and we will have to modify the text."),
        required=False,
    )


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class EventInfo(Container):
    grok.implements(IEventInfo)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IEventInfo)
    grok.require('zope2.View')
    grok.name('view')


# create index and metadata
@indexer(IEventInfo)
def signUpFrom_indexer(obj):
    return obj.signUpFrom
grok.global_adapter(signUpFrom_indexer, name='signUpFrom')

@indexer(IEventInfo)
def signUpEnd_indexer(obj):
    return obj.signUpEnd
grok.global_adapter(signUpEnd_indexer, name='signUpEnd')

@indexer(IEventInfo)
def happenDate_indexer(obj):
    return obj.happenDate
grok.global_adapter(happenDate_indexer, name='happenDate')

@indexer(IEventInfo)
def eventCategory_indexer(obj):
    return obj.eventCategory
grok.global_adapter(eventCategory_indexer, name='eventCategory')
