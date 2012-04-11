import sys,urllib
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

class NetworkAccessManager(QNetworkAccessManager):
	def __init__(self,old_manager):
		QNetworkAccessManager.__init__(self)
		self.old_manager = old_manager
		self.setCache(old_manager.cache())
		self.setCookieJar(old_manager.cookieJar())
		self.setProxy(old_manager.proxy())
		self.setProxyFactory(old_manager.proxyFactory())
		self.count=0
	
	def createRequest(self, operation, request, data):
		#print "request"
		#if request.hasRawHeader(QByteArray(QString("Content-type").toAscii())):
		#if request.url().toString().contains("mp4"):
		if request.url().path().endsWith("mp4"):
			print request.url()
			urllib.urlretrieve(str(request.url().toString()),str(self.count)+".mp4")
			self.count=self.count+1
		reply=QNetworkAccessManager.createRequest(self,operation, request, data)
		#content_type=reply.header(QNetworkRequest.ContentTypeHeader).toString()
		#if(content_type.contains("video")):
		#	print content_type
		#print content_type
		return reply
		

def main():
	app=QApplication(sys.argv)
	#enable the flash player plugin, firefox and flash plugin must be installed
	QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True);
	view=QWebView()
	old_manager=view.page().networkAccessManager()
	new_manager=NetworkAccessManager(old_manager)
	view.page().setNetworkAccessManager(new_manager)
	url="http://v.youku.com/v_show/id_XMzAzMzIzMjky.html"
	#url="http://v.ku6.com/show/25_1-iWIWGQB2nTN.html"
	#url="http://www.zhizhen.com/book/read.jhtml?e=b4d5b4448de2c91ef126acc56a2b75092156ded9c0a2eef0dd7f56c97354b262"
	#mframe=page.mainFrame()
	#mframe.load(QUrl(url))
	view.load(QUrl(url))
	view.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()      
