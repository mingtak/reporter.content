from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SearchContent(BrowserView):

    template = ViewPageTemplateFile('templates/searchContent.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog

        # search by grade
        try:
            if hasattr(request, 'grade'):
                gradeList = getattr(request, 'grade', '').split('_')
                if gradeList == ['']:
                    self.brainForGrade = None
                gradeIndex = []
                for index in gradeList:
                    gradeIndex.append(int(index)) 
                self.brainForGrade = catalog({'grade':gradeIndex})
            else:
                self.brainForGrade = None
        except:
            self.brainForGrade = None
            pass
        return self.template()
