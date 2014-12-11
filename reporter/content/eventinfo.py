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


from reporter.content import MessageFactory as _


class IEventInfo(form.Schema, IImageScaleTraversable):
    """
    Event information content type
    """
    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_eventinfo_image",
                      default=u"Please upload event image, if have."),
        required=False,
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

    eventDate = schema.Date(
        title=_(u"Event date"),
        description=_(u"help_eventinfo_Date",
                      default=u"Event happen date, if have."),
        required=False,
    )

    text = RichText(
        title=_(u"Notice content"),
        description=_(u"help_notice_text",
                      default=u"We will comfirm this notice, then publish it, and we will have to modify the text."),
        required=False,
    )


class EventInfo(Container):
    grok.implements(IEventInfo)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IEventInfo)
    grok.require('zope2.View')
    # grok.name('view')
