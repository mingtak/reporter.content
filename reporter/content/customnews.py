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

# plone.api
from plone import api

# index and metadata
from plone.indexer import indexer
from collective import dexteritytextindexer

# for add/edit form
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# i18n
from reporter.content import MessageFactory as _


@grok.provider(IContextSourceBinder)
def availableAuthor(context):
    current_user = api.user.get_current().id
    brain = context.portal_catalog({"portal_type":"reporter.content.author",
                                    "Creator":current_user})
    terms = []
    for item in brain:
        terms.append(SimpleVocabulary.createTerm(item.UID, item.UID, item.Title))
    return SimpleVocabulary(terms)


class ICustomNews(form.Schema, IImageScaleTraversable, INewsItem):
    """
    Custom news content type, inherit from News.
    """
    author = schema.Choice(
        title=_(u"Author"),
        source=availableAuthor,
        required=False,
    )

    grade = schema.Int(
        title=_(u'label_grade', default=u"input author's grade."),
        description=_(u'help_grade',
                      default=u"How grade at now? Please input author's grade(1-9)."),
        min=1,
        max=9,
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_image",
                      default=u"Please upload lead image, this image will show in cover."),
        required=False,
    )

    imageContribute = schema.Bool(
        title=_(u"Image contribute"),
        description=_(u"help_imageContribute",
                      default=u"if you want contribute this image for homoe page conver, please check it. If approved, we will show post to Facebook"),
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


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class CustomNews(Container):
    grok.implements(ICustomNews)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ICustomNews)
    grok.require('zope2.View')
    grok.name('view')

    def getAuthor(self):
        catalog = self.context.portal_catalog
        author = catalog(UID=self.context.author)[0]
        return author


# create index and metadata
@indexer(ICustomNews)
def authorUID_indexer(obj):
    authorUID = obj.author
    return authorUID
grok.global_adapter(authorUID_indexer, name='authorUID')

@indexer(ICustomNews)
def imageContribute_indexer(obj):
    imageContribute = obj.imageContribute
    return imageContribute
grok.global_adapter(imageContribute_indexer, name='imageContribute')

@indexer(ICustomNews)
def grade_indexer(obj):
    grade = obj.grade
    return grade
grok.global_adapter(grade_indexer, name='grade')
