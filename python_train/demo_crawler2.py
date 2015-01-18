import sys
class UrlRequest:
    def __init__(self,request_url):
        try: 
            urllib2
        except:
            import urllib2
        request = urllib2.Request(request_url)
        try:
            response = urllib2.urlopen(request)
        except:
            print 'URL : ' + sys.argv[1] + ' doesn\'t exists'
            raise sys.exit()
        self.read = response.read()

class ReCompile:
    def __init__(self,file_ext):
        try:
            re
        except:
            import re
        self.file_ext = file_ext
        self.img_filter1 = re.compile('https?:\/+[a-zA-Z0-9./&%=-_]+\.jpg|https?:\/+[a-zA-Z0-9./&%=-_]+\.gif|https?:\/+[a-zA-Z0-9./&%=-_]+\.png')
        self.img_filter2 = re.compile('[a-zA-Z0-9./&%=-_]+\.jpg|[a-zA-Z0-9./&%=-_]+\.gif|[a-zA-Z0-9./&%=-_]+\.png')
        self.domain_filter = re.compile('https?://[a-zA-Z0-9.]*')
    def find(self,url_read, req_url = None):
        img_links = []
        domain = self.domain_filter.findall(sys.argv[1])[0]
        if self.file_ext == 'img':
            for img_link in self.img_filter1.findall(url_read):
                img_links.append('<img src="'+img_link+'" />')
            self.img_filter2.sub(' ', url_read)
            for img_link in self.img_filter2.findall(url_read):
                img_links.append('<img src="'+sys.argv[1]+img_link[1:]+'" />')
                img_links.append('<img src="'+domain+img_link+'" />')
        return img_links
in_req = UrlRequest(sys.argv[1])
print sys.argv[1]
img_filter = ReCompile('img') 
try:
    f = open(sys.argv[2]+'.html','a+')
except:
    f = open('tmp.html', 'a+')
try:
    f.write('<!DOCTYPE html">\
             <html">\
             <head>\
             <title>'+sys.argv[1]+' :: Image Crawler'+'</title>\
             </head>\
             <body>')
    for img_link in img_filter.find(in_req.read, sys.argv[1]):
        f.write(img_link + "\n")
    f.write('</body>\
             </html>')
except:
    print 'Failed file write'
    raise sys.exit()
finally:
    print 'Succefully make html file'
f.close()

