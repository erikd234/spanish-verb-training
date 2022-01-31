"""
    Class for web scrawler which gets web pages from a given URL. 
"""

import requests


class WebCrawler:
    def __init__(self):
        pass

    def crawl_page(self, url):
        html = self.fetch_html(url)
        return html

    def fetch_html(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Bad Request - response code: {response.status_code}")
        return response.content
