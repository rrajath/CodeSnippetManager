'''
Created on Aug 24, 2013

@author: rajath
'''

import xml.dom.minidom
import time
import re

class Snippet:

    xml = ''
    data = ''
    
    # search snippet
    #   search by tags
    #   search by language
    #   search by title
    #   search by date (that is, from some date onwards)

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

    # Prettifying XML before storing it in a file
    def prettify(self):
        self.xml = xml.dom.minidom.parseString(self.data).toprettyxml() # or xml.dom.minidom.parseString(xml_string)
        return self.xml

    # Write the snippet to the output file
    def save_snippet(self):
        with open("data/code.xml",'w') as f:
            f.write(self.prettify())
