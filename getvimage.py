import sys
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import time,os,codecs,random
br = mechanize.Browser()
# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
url="http://www.yuntushuguan.com/vImage.jsp"
i=0
while(True):
    i=i+1
    r=br.open_novisit(url)
    imd=r.read()
    f=open(str(i)+".jpg",'w')
    f.write(imd)
    f.close()
    time.sleep(2)