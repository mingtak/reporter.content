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


whichCity = SimpleVocabulary(
    [SimpleTerm(value=u'Taipei', title=_(u'Taipei')),
     SimpleTerm(value=u'New Taipei', title=_(u'New Taipei')),
     SimpleTerm(value=u'Keelung', title=_(u'Keelung')),]
    )


class IAuthor(form.Schema, IImageScaleTraversable):
    """
    Define Author(student)
    """
    image = NamedBlobImage(
        title=_(u"Author picture"),
        required=False,
    )

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

    """
    grade = schema.Int(
        title=_(u'label_grade', default=u"input author's grade."),
        description=_(u'help_grade',
                      default=u"Please input author's grade(1-9)."),
        min=1,
        max=9,
        required=False,
    )

    className = schema.TextLine(
        title=_(u'label_className', default=u"input author's class name."),
        description=_(u'help_className',
                      default=u"Please input author's class name."),
        max_length=3,
        required=False,
    )
    """


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class Author(Container):
    grok.implements(IAuthor)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IAuthor)
    grok.require('zope2.View')
    # grok.name('view')
