"""
    Class for parsing an html page and creating the Verb tree (see create_verb_tree_examples)

    see https://www.crummy.com/software/BeautifulSoup
    see https://pandas.pydata.org/docs/
"""

from bs4 import BeautifulSoup


class VerbParser:
    def __init__(self):
        self.html_soup = object()

    def create_verb_tree(self, page_content):
        self.set_html_soup(page_content)
        if not self.is_valid_verb_page():
            return {"message": "Word is not a verb"}

        # proceed! Now we need to parse some verb trees

    def set_html_soup(self, page_content):
        self.html_soup = BeautifulSoup(page_content, "html.parser")

    def is_valid_verb_page(self):
        meta_tags = self.html_soup["head"].find_all("meta")
        is_verb_page = False
        for tag in meta_tags:
            if "name" in tag.attrs and tag["name"] == "description":
                is_verb_page = "Conjugate" in tag["content"]
                break
        return is_verb_page
