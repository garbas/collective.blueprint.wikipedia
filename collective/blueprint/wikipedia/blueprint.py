
from zope.interface import implements
from zope.interface import classProvides
from zope.component import queryUtility

from plone.i18n.normalizer.interfaces import IURLNormalizer
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection

from lxml import etree


class Wikipedia(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous, self.options = previous, options

    def __iter__(self):
        for item in self.previous:
            yield item

        if not self.options.get('xml', None):
            return
        
        base_path = self.options.get('base-path', '')+'/'
        locale = self.options.get('locale', None)
        normalize = queryUtility(IURLNormalizer).normalize

        j = 1
        fxml = open(self.options['xml'])
        context = etree.iterparse(fxml, tag="page")
        for action, element in context:
            title = [i for i in element.iter(tag='title')][0].text
            # due to some errors we put this debug notice in try..except
            try:
                print str(j)+': ('+str(type(title))+')'+title
            except:
                pass
            text = unicode([i for i in element.iter(tag='text')][0].text).encode('utf-8')
            yield dict(_type = 'Document',
                       _path = base_path+normalize(title),
                       title = title,
                       text = text,)
            j += 1
            element.clear()
            parent = element.getparent()
            previous_sibling = element.getprevious()
            while previous_sibling is not None:
                parent.remove(previous_sibling)
                previous_sibling = element.getprevious()

        fxml.close()




