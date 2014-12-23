from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from zope import schema
from plone.directives import form as Form
# for i18n
from reporter.content import MessageFactory as _


class IPageEnvSetting(Form.Schema):
    topBanner = schema.Text(
        title=_(u"Top banner setting"),
        required=False,
    )


class PageEnvSettingControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IPageEnvSetting

PageEnvSettingControlPanelView = layout.wrap_form(PageEnvSettingControlPanelForm, ControlPanelFormWrapper)
PageEnvSettingControlPanelView.label = _(u"Page Env setting control panel form")
