from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from zope import schema
from plone.directives import form as Form
# for i18n
from reporter.content import MessageFactory as _


class IHomepageLayoutSetting(Form.Schema):
    slideSetup = schema.Text(
        title=_(u"Homepage slide setting"),
        required=False,
    )

    eventSetup = schema.Text(
        title=_(u"Homepage event setting"),
        required=False,
    )

    competitionSetup = schema.Text(
        title=_(u"Homepage competition setting"),
        required=False,
    )

    articleSetup = schema.Text(
        title=_(u"Homepage article setting"),
        required=False,
    )

    customNewsSetup = schema.Text(
        title=_(u"Homepage customNews setting"),
        required=False,
    )


class HomepageLayoutSettingControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IHomepageLayoutSetting

HomepageLayoutSettingControlPanelView = layout.wrap_form(HomepageLayoutSettingControlPanelForm, ControlPanelFormWrapper)
HomepageLayoutSettingControlPanelView.label = _(u"Homepage layout setting control panel form")
