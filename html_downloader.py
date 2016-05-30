__author__ = 'worker'

import  urllib2

class HtmlDownloader(object):
    def downloadPage(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return  None

        return response.read()

    def downloadImage(self, url, dir):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return False

        try:
            filename = dir + "/" + url.split('/')[-1]
            f = open(filename, 'wb')
            f.write(response.read())

            return True
        except Exception, e:
            return False
        finally:
            f.close()
        
        