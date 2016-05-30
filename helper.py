__author__ = 'worker'

import traceback, urllib2, os, sys
import html_downloader, html_parser, html_outputer

class LvyeOrgHelper(object):
    def __init__(self):
        self.lvye_id = ""
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def download(self):
        # search id page
        # https://www.google.com/search?q=老纳 统计信息 site:www.lvye.org"
        url = u"https://www.google.com/search?q=%s 统计信息 site:www.lvye.org" % self.lvye_id
        url = url.encode('utf-8')
        print url
        
        html_cont = self.downloader.downloadPage(url)
        filename = dir + "/" + self.lvye_id + ".html"
        print filename
        f = open(filename, 'wb')
        f.write(html_cont)

        # for debug
        return True

        # parse cache url
        cache_url = self.parser.parse_cache_url(url, html_cont)
        if cache_url is None:
            return False

        html_cont = self.downloader.downloadPage(cache_url)

        # save to file
        dir = "%s/download/%s" % (os.getcwd(), self.lvye_id)
        if not os.path.exists(dir):
            os.makedirs(dir)

        try:
            filename = dir + "/" + self.lvye_id + ".html"
            f = open(filename, 'wb')
            f.write(html_cont)

            return True
        except Exception, e:
            return False
        finally:
            f.close()

    def print_usage(self):
        print "Usage:\n"
        print "python %s <lvyeid>\n" % sys.argv[0]
        print "e.g.\n"
        print "python %s 老纳" % sys.argv[0]

if __name__ == "__main__":
    obj_helper = LvyeOrgHelper()

    if len(sys.argv) <= 1:
        obj_helper.print_usage()
    else:
        self.lvye_id = sys.argv[1]
        obj_helper.download(self.lvye_id)
    