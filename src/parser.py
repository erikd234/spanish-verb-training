"""
    Class for parsing an html page and creating the Verb tree (see create_verb_tree_examples)
"""

from bs4 import BeautifulSoup


class VerbParser:
    def __init__(self):
        self.html_soup = object()

    def create_verb_tree(self, page_content):
        self.parse_html(page_content)

        if not self.meta_data_contains_keyword("conjugate"): 
            return { "message" : "Word is not a verb" } 

 
    def parse_html(self, page_content):
        self.html_soup = BeautifulSoup(page_content, "html.parser")

    def meta_data_contains_keyword(keyword): 
        return True

