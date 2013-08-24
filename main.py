'''
Created on Aug 24, 2013

@author: rajath
'''
from CodeSnippetManager import Snippet

def main():
    print 'Code Snippet Manager.'
    title = raw_input('Enter Title: ')
    lang = raw_input('Enter Language: ')
    desc = raw_input('Enter Description: ')
    code = raw_input('Enter Code: ')
    tags = raw_input('Enter Tags (comma separated): ')

    snippet = Snippet()

    snippet.add_code(code)
    snippet.add_date()
    snippet.add_desc(desc)
    snippet.add_language(lang)
    snippet.add_tags(tags)
    snippet.add_title(title)
    snippet.add_snippet()
    
    snippet.save_snippet()
    
if __name__ == '__main__':
    main()