import os,sys,urllib
def getThumbImg(itemId):
    id=(9-len(itemId))*'0'+itemId
    ids=id[0:3]+'/'+id[3:6]+'/'+id[6:]+'/'   
    imgurl="http://i2.tdimg.com/"+ids+"p.jpg"
    print imgurl
    urllib.urlretrieve(imgurl,id+'.jpg')
    
if __name__=="__main__":
    f=open('itemids.txt','r')
    for i in f.readlines():
        getThumbImg(i.strip('\n').strip())
    f.close()