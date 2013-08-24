'''
Created on Aug 24, 2013

@author: rajath
'''
from CodeSnippetManager import Snippet
import sys

def main():
    print 'Code Snippet Manager'

    snippet = Snippet()
        
    if len(sys.argv) != 3:
        print 'Usage: python main.py -s foo'
    else:
        if sys.argv[1] in ['-s','--search']:
            keyword = sys.argv[2]
            snippet.search(keyword)
            print 'Exiting...Done'
            sys.exit(0)
        else:
            print 'Usage: python main.py -s foo'

    choice = input('What do you want to do?\n1. Add\n2. Lookup\n3. Exit')

    if choice == 1:
        title = raw_input('Enter Title: ')
        snippet.add_title(title)
        desc = raw_input('Enter Description: ')
        snippet.add_desc(desc)
        lang = raw_input('Enter Language: ')
        snippet.add_language(lang)
        code = raw_input('Enter Code: ')
        snippet.add_code(code)
        tags = raw_input('Enter Tags (comma separated): ')
        snippet.add_tags(tags)
        snippet.add_date()
    
        snippet.add_snippet()

    elif choice == 2:
        keyword = raw_input('Enter Keyword: ')
        snippet.search(keyword)

    else:
        print 'Exiting... Done'
        sys.exit(0)
    
if __name__ == '__main__':
    main()