import urllib,cookielib,re,os
import os.path
from xml.etree.ElementTree import ElementTree,fromstring,tostring

def getVideo(id,video_name):
	id=id.strip('\n')
	#video_name="E:/videos/negative/"+id+".f4v"
	if not os.path.exists(video_name):
		url="http://v2.tudou.com/v?it="+id
		cj=cookielib.CookieJar()
		r=urllib.urlopen(url)
		html=r.read()
		#print html
		pr=re.compile("http://(?:.|\n)*?</f>")
		ma=re.search(pr,html)
		if(ma==None):
			return
		myxml=fromstring(html)
		try:
			title=myxml.get('title')
		except:
			return
		#video_url=myxml[0][0].text
		video_url=ma.group(0)[:-4]
		#print video_url
		
		#video_name=id+".f4v"
		#fo.write(id+" "+title.encode("utf-8")+"\n")
		#print id,title
		#print video_name
		try:
			urllib.urlretrieve(video_url,video_name)
		except:
			return

if __name__=='__main__':
	for pa,dn,fn in os.walk("E:/videos/positive"):
		#print pa,pa[:20]
		for j in dn:
			itemId=j[:9]
			name=pa+"/"+j+"/"+itemId+"tudou.f4v"
			getVideo(itemId,name)