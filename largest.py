import urllib,cookielib,re,os
from xml.etree.ElementTree import ElementTree,fromstring,tostring

def getIdTitles():
    f=open("keyslist-load.txt","r")
    fo=open("idtilte2.lst","w")
    max=0
    for i in f.readlines():
	i=i.strip("\n")
	url="http://v2.tudou.com/v?it="+i
	cj=cookielib.CookieJar()
	r=urllib.urlopen(url)
	html=r.read()
	#print html
	pr=re.compile("http://(?:.|\n)*?</f>")
	ma=re.search(pr,html)
	if(ma==None):
		continue
	myxml=fromstring(html)
	try:
		title=myxml.get('title')
	except:
		continue
	#video_url=myxml[0][0].text
	video_url=ma.group(0)[:-4]
	#print video_url
	
	#video_name=id+".f4v"
	fo.write(i+" "+title.encode("utf-8")+"\n")
    
    fo.close()
    f.close()
    
if __name__=='__main__':
    getIdTitles()