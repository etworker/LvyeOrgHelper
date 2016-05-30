#coding=utf-8
__author__ = 'worker'

import urlparse
import re
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse_cache_url(self, page_url, html_cont):
        if (page_url is None ) or (html_cont is None):
            return None

        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        links = soup.find_all("div", attrs={"class": "post_thumbnail_container has_imageurl"})
        for link in links:
            try:
                # new_url = link["data-imageurl"]
                print link
            except:
                continue

        return link