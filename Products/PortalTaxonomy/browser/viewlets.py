from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

FORM_TITLE = 'Resource Collections'

class SmartSearchViewlet(ViewletBase):
    render = ViewPageTemplateFile('smart_search.pt')

    def update(self):
        self.FormTitle = FORM_TITLE
        self.portal_props = getToolByName(self.context, 'portal_properties')
        self.props = getattr(self.portal_props, 'site_properties')
        self.desc_length = self.props.search_results_description_length
        self.desc_ellipsis = self.props.search_results_description_length
        self.use_view_action = self.props.typesUseViewActionInListings
