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


class ICompetition(form.Schema, IImageScaleTraversable):
    """
    Competition content type
    """
    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_competition_image",
                      default=u"Please upload competition image, if have."),
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

    competitionDate = schema.Date(
        title=_(u"Competition date"),
        description=_(u"help_competitionDate",
                      default=u"CompetitionDate date, if have."),
        required=False,
    )

    text = RichText(
        title=_(u"Notice content"),
        description=_(u"help_notice_text",
                      default=u"We will comfirm this notice, then publish it, and we will have to modify the text."),
        required=False,
    )

class Competition(Container):
    grok.implements(ICompetition)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ICompetition)
    grok.require('zope2.View')
#    grok.name('view')
