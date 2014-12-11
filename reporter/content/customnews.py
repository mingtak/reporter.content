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
from plone.app.contenttypes.interfaces import INewsItem

from reporter.content import MessageFactory as _


# Interface class; used to define content-type schema.

class ICustomNews(form.Schema, IImageScaleTraversable, INewsItem):
    """
    Custom news content type, inherit from News.
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

    newsImage_1 = NamedBlobImage(
        title=_(u"News image 1"),
        required=False,
    )

    newsImage_2 = NamedBlobImage(
        title=_(u"News image 2"),
        required=False,
    )


class CustomNews(Container):
    grok.implements(ICustomNews)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ICustomNews)
    grok.require('zope2.View')
    # grok.name('view')
