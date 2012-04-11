import urllib,cookielib,re,os
from xml.etree.ElementTree import ElementTree,fromstring,tostring
def getVideo(id,done):
	id=id.strip('\n')
	#video_name="/home/is_admin/videos/"+id+".f4v"
	video_name="E:/newvideos/"+id+".f4v"
	#print video_name 
	#return
	if not os.path.exists(video_name) and id not in done:
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
		#try:
		#	title=myxml.get('title')
		#except:
		#	return
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
	f=open("keyslist-all.txt")
	fo=open("D:/videos/downloaded.txt","r")
	done=[]
	for i in fo.readlines():
		it=i.strip("\n")
		done.append(it)
	fo.close()
	fo=open("D:/refer/refer.txt","r")
	for i in fo.readlines():
		it=i.strip("\n")
		done.append(it)
	fo.close()
	for i in f.readlines():
		#print i
		getVideo(i,done)
	f.close()