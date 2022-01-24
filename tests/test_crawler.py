"""
    tests for web crawler
"""
import pytest
from src.crawler import WebCrawler


def test_create_web_crawler():
    crawler = WebCrawler()
    assert isinstance(crawler, WebCrawler)


def test_crawler_with_good_url():
    """
    Regular test case
    """
    crawler = WebCrawler()
    url = "https://www.spanishdict.com/conjugate/hablar"
    result_html = crawler.crawl_page(url)
    assert result_html


def test_crawler_throws_exception():
    crawler = WebCrawler()
    test_invalid_url = "https://www.spanishdict.com/doesn%20exist"

    with pytest.raises(Exception):
        crawler.crawl_page(test_invalid_url)
