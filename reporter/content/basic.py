from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from z3c.form.interfaces import IEditForm, IAddForm
from plone.autoform import directives as form

from reporter.content import MessageFactory as _
#from plone.app.dexterity import PloneMessageFactory as _PMF

class IBasic(model.Schema):
    """
       Marker/Form interface for Basic
    """
    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        description=_(
            u'help_title',
            default=u"Please input author's name or nickname."
        ),
        required=True
    )

    description = schema.Text(
        title=_(u'label_description', default=u'Summary'),
        description=_(
            u'help_description',
            default=u'Used in item listings and search results, max length is 200.'
        ),
        max_length=200,
        required=False,
        missing_value=u'',
    )

    form.order_before(description='*')
    form.order_before(title='*')

    form.omitted('title', 'description')
    form.no_omit(IEditForm, 'title', 'description')
    form.no_omit(IAddForm, 'title', 'description')



alsoProvides(IBasic, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class Basic(object):
    """
       Adapter for Basic
    """
    implements(IBasic)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    def _get_title(self):
        return self.context.title

    def _set_title(self, value):
        if isinstance(value, str):
            raise ValueError('Title must be unicode.')
        self.context.title = value
    title = property(_get_title, _set_title)

    def _get_description(self):
        return self.context.description

    def _set_description(self, value):
        if isinstance(value, str):
            raise ValueError('Description must be unicode.')
        self.context.description = value
    description = property(_get_description, _set_description)
