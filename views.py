import os,MySQLdb,sys
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

db=MySQLdb.connect(user="root",passwd="123456",db="test")
c=db.cursor()
i=0
d={}
while(i<100):
    l=[]
    c.execute("select matchId from result where jobId=%s;"%i)
    while(a=c.fetchone()):
        b=list(a)
        for i in b:
            if i!=-1:
                l.append(getThumbImg(i))
        d[i]=l
        
def getThumbImg(itemId):
    id=(9-len(str(itemId)))*'0'+str(itemId)
    ids=id[0:3]+'/'+id[3:6]+'/'+id[6:]+'/'   
    imgurl="http://i2.tdimg.com/"+ids+"p.jpg"
    return imgurl
    
def main_page(request):
    return render_to_response("main.html",{'matchResultList',d})
        
                
            
        