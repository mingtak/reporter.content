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


whichCity = SimpleVocabulary(
    [SimpleTerm(value=u'Taipei', title=_(u'Taipei')),
     SimpleTerm(value=u'New Taipei', title=_(u'New Taipei')),
     SimpleTerm(value=u'Keelung', title=_(u'Keelung')),]
    )


class IAuthor(form.Schema, IImageScaleTraversable):
    """
    Define Author(student)
    """

    city = schema.Choice(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"Select a city where school is?"),
        vocabulary=whichCity,
        required=False,
        )

    schoolName = schema.TextLine(
        title=_(u'label_schoolname', default=u"input your school name."),
        description=_(u'help_schoolname',
                      default=u"Please input your school name."),
        required=False,
        )

    className = schema.TextLine(
        title=_(u'label_className', default=u"input your class name."),
        description=_(u'help_className',
                      default=u"Please input your class name."),
        required=False,
        )



class Author(Container):
    grok.implements(IAuthor)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IAuthor)
    grok.require('zope2.View')
    # grok.name('view')
