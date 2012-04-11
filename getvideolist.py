from BeautifulSoup import BeautifulSoup
import mechanize,re,urllib
def getVideo(sw,fo):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    #br.open("http://cn.bing.com/?scope=video&FORM=Z9LH1")
    #br.select_form(nr=0)
    #br.form['q']="Girls Generation"
    #rb=br.open("http://cn.bing.com/videos/search?pq=girls+generation&sc=8-16&sp=-1&sk=&qpvt=Girls+Generation&q=Girls+Generation%20filterui:msite-youku.com&FORM=R5FD8")
    #http://cn.bing.com/videos/search?pq=girls+generation&sc=8-16&sp=-1&sk=&qpvt=Girls+Generation&q=Girls+Generation%20filterui:msite-youku.com&FORM=R5FD9
    #rb=br.open("http://cn.bing.com/videos/search?pq=girls+generation&sc=8-16&sp=-1&sk=&qpvt=Girls+Generation&q=Girls+Generation%20filterui:msite-ku6.com&FORM=R5FD1")
    #http://cn.bing.com/videos/search?pq=girls+generation&sc=8-16&sp=-1&sk=&qpvt=Girls+Generation&q=Girls+Generation%20filterui:msite-6.cn&FORM=R5FD12
    #rb=br.submit()
    #vsite=['youku','ku6']
    #replace the space in search word
    #sw
    #for site in vsite:
        #surl="http://cn.bing.com/videos/search?pq=%s&sc=8-16&sp=-1&sk=&qpvt=Girls+Generation&q=Girls+Generation%20filterui:msite-%s.com&FORM=R5FD8"%site
        #rb=br.open(surl)
        #http://cn.bing.com/videos/search?q=%E9%92%A2%E9%93%81%E4%BE%A0&go=&qs=n&form=QBLH&pq=%E9%92%A2%E9%93%81%E4%BE%A0&sc=0-4&sp=-1&sk=
    #sw=sw.replace(" ","+")
    #sw=sw.decode("utf-8")
    #sw=sw.encode("gb2312")
    sw=urllib.quote(sw)
    longtime=urllib.quote(" filterui:duration-long")
    #rb=br.open("http://cn.bing.com/videos/search?q=%E8%80%81%E5%A4%A7%E7%9A%84%E5%B9%B8%E7%A6%8F34&go=&qs=n&form=QBLH&pq=%E8%80%81%E5%A4%A7%E7%9A%84%E5%B9%B8%E7%A6%8F34&sc=1-7&sp=-1&sk=")
    #http://cn.bing.com/videos/search?pq=%u65b9%u8c2c%u795e%u63a206&sc=0-0&sp=-1&sk=&qpvt=%E6%96%B9%E8%B0%AC%E7%A5%9E%E6%8E%A206&q=%E6%96%B9%E8%B0%AC%E7%A5%9E%E6%8E%A206%20filterui:duration-long&FORM=R5FD2
    surl="http://cn.bing.com/videos/search?q=%(sw)s&go=&qs=n&form=Z9LH1&pq=%(sw)s%(longtime)s&sc=1-7&sp=-1&sk="%{"sw":sw,"longtime":longtime}
    print surl
    rb=br.open(surl)
    content = rb.read()
    vr=re.compile("purl=\"http://(?:.|\n)*?\"")
    #vr=re.compile("result-link\"\ href=\"http://(?:.|\n)*?\"")
    #vr=re.compile("result-link")
    #vr['youku']=re.compile("http://v.youku.com/v_show/id_(?:.|\n)*?.html")
    #vr['ku6']=re.compile("http://v.ku6.com/show/(?:.|\n)*?.html")
    ma=re.findall(vr,content)
    print len(ma)
    for i in ma:
        if i.find("tudou")==-1 and i.find("cntv")==-1 and i.find("xinhuanet")==-1:
            print i[6:-1]
            fo.write(i[6:-1]+"\n")

def main():
    f=open("idtilte2.lst")
    fo=open("videopage2.lst","w")
    for sw in f.readlines():
        l=sw.find(" ")
        title=sw[l:]
        getVideo(title,fo)
    fo.close()
    
if __name__=="__main__":
    main()   

#import os
#os.chdir("E:/videos")
#from kw2vlBaidu import *
