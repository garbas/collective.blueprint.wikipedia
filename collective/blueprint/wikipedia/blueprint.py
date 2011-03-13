
import re
import logging

from zope.interface import implements
from zope.interface import classProvides

from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection

from lxml import etree
logger = logging.getLogger('wikipedia import')

XMLNS = '{http://www.mediawiki.org/xml/export-0.4/}'
WIKI_PATTERN = re.compile(r'\[\[([\w\W]+?)\]\]')

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

        start_at_number = int(self.options.get('start-at-number', 1))
        stop_at_number = int(self.options.get('stop-at-number', 0))
        commit_at_every = int(self.options.get('commit-at-every', 0))

        j = 1
        fxml = open(self.options['xml'])
        context = etree.iterparse(fxml, tag=XMLNS+"page")
        for action, element in context:

            title = [i for i in element.iter(tag=XMLNS+'title')][0].text
            text = unicode([i for i in element.iter(tag=XMLNS+'text')][0].text).encode('utf-8')

            # remove i18n wiki links from text
            for i in WIKI_PATTERN.findall(text):
                if  ':' not in i or \
                   (':' in i and i[i.find(':')-1] == '\\'):
                    continue
                if len(i.split(':')[0]) != 2:
                    continue
                if text[text.find(i)-3] == '\n':
                    text = text.replace('\n[['+i+']]', '')
                elif text.find(i)+len(i)+2 < len(text) and \
                     text[text.find(i)+len(i)+2] == '\n':
                    text = text.replace('[['+i+']]\n', '')
                else:
                    text = text.replace('[['+i+']]', '')

            j += 1
            if j < start_at_number:
                continue
            logger.warn(str(j-1)+': '+title)
            if title == 'Angiography':
                import ipdb; ipdb.set_trace()

            yield dict(
                    _wiki_title = title,
                    _wiki_text = text,
                    )

            if j == stop_at_number and stop_at_number != 0:
                break
            if commit_at_every != 0 and (j-1) % commit_at_every == 0:
                logger.warn( ('*'*10) + ' COMMITING ' + ('*'*10) )
                import transaction; transaction.commit()

            element.clear()
            parent = element.getparent()
            previous_sibling = element.getprevious()
            while previous_sibling is not None:
                parent.remove(previous_sibling)
                previous_sibling = element.getprevious()

        fxml.close()




