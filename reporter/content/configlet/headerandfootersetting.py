from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from zope import schema
from plone.directives import form as Form
# for i18n
from reporter.content import MessageFactory as _


class IHeaderAndFooterSetting(Form.Schema):
    aboutUs = schema.Text(
        title=_(u"About us setting"),
        required=False,
    )

    hotTags = schema.Text(
        title=_(u"Hot tags"),
        required=False,
    )


class HeaderAndFooterSettingControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IHeaderAndFooterSetting

HeaderAndFooterSettingControlPanelView = layout.wrap_form(HeaderAndFooterSettingControlPanelForm, ControlPanelFormWrapper)
HeaderAndFooterSettingControlPanelView.label = _(u"Header and footer setting control panel form")
