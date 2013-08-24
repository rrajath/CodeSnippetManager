'''
Created on Aug 24, 2013

@author: rajath
'''

import xml.dom.minidom
import libxml2
import time
import re

class Snippet:

    xml = ''
    data = ''
    results = []

    # Add XML declaration in case the file is created for the first time
    def __init__(self):
        self.xml_decl = '<?xml version="1.0" encoding="UTF-8" ?><root>'

    # Add title to the snippet    
    def add_title(self, title):
        self.title = '<title>' + title + '</title>'

    # Add which language the snippet belongs to. Comes in handy while searching    
    def add_language(self, language):
        self.language = '<lang>' + language + '</lang>'

    # Add description about what the snippet does    
    def add_desc(self, desc):
        self.desc = '<desc>' + desc + '</desc>'

    # Add code snippet.    
    def add_code(self, code):
        self.code = '<code>' + code + '</code>'
        self.code = self.code.replace('&amp;','&')
        self.code = self.code.replace('&quot;','"')

    # Record date and time of creation of code snippet    
    def add_date(self):
        self.date = '<date>' + time.ctime() + '</date>'

    # Add tags for easy searching    
    def add_tags(self, tags):
        self.tags = tags

    # Appending snippets to the already existing list of code snippets
    def add_snippet(self):
        self.snippet = '<snippet tags = "' + self.tags + '">' + self.title + self.language + self.desc + self.code + self.date + '</snippet></root>'
        try:
            with open("data/code.xml") as f:
                self.data = f.read()
                self.data = self.data.replace('\n','')
                pattern = re.compile(r'>\s+<')
                self.data = re.sub(pattern, '><', self.data)
                self.data = self.data.replace('</root>',self.snippet)
        except:
            self.data = self.xml_decl + self.snippet
        self.save_snippet()

    # Prettifying XML before storing it in a file
    def prettify(self):
        self.xml = xml.dom.minidom.parseString(self.data).toprettyxml() # or xml.dom.minidom.parseString(xml_string)
        return self.xml

    # Write the snippet to the output file
    def save_snippet(self):
        with open("data/code.xml",'w') as f:
            f.write(self.prettify())
        print 'Code Snippet added to Library'
        print 'File generated (for reference) at: data/code.xml'

    # TODO: split tags and search individual tags to get the best match (in descending order)
    # Search everything
    def search(self, keyword):
        doc = libxml2.parseFile('data/code.xml')
        self.results = []
        for node in doc.xpathEval('//snippet'):
            if keyword in str(node):
                self.results.append(node)
        self.show_results()

    # Display output
    def show_results(self):
        count = len(self.results)
        print
        print count, 'code snippet(s) found:'
        # Display contents of each tag.
        for snippet in self.results:
            doc = libxml2.parseDoc(str(snippet))
            print '-'*50
            print 'Title:', self.getContent(doc, 'title')
            print 'Description:', self.getContent(doc, 'desc')
            print 'Language:', self.getContent(doc, 'lang')
            print 'Code:', self.getContent(doc, 'code')
            print 'Date:', self.getContent(doc, 'date')
            print 'Tags:', self.getTags(doc, 'tags')

    # Get contents of an element    
    def getContent(self, doc, element):
        for i in doc.xpathEval('//' + element):
            return i.content
    
    # Get contents of a tag
    def getTags(self, doc, tags):
        for i in doc.xpathEval('//@tags'):
            return i.content