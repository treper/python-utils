import os,glob
import cv
d={'2':0,'3':1,'4':2,'7':3,'8':4,'a':5,'d':6,'e':7,'k':8,'m':9,'n':10,'p':11,'s':12,'w':13,'x':14}
c=0
f=open('test.txt','w')
for k in d.keys():
    dir='/home/ataosky/workspace/vimages/test/'+k
    #os.system("cd %s"%dir)
    os.chdir(dir)
    #print 'cd to %s'%dir
    jpg_list=glob.glob('*.jpg')
    for i in jpg_list:
        c=c+1
        im=cv.LoadImage(i,0)
        im2=cv.CreateImage(cv.GetSize(im),cv.IPL_DEPTH_8U,1)
        cv.Threshold(im,im2,100,255,cv.CV_THRESH_BINARY)
        ima=cv.GetMat(im2)
        for ii in range(0,32):
            for jj in range(0,32):
                f.write(str(ima[ii,jj])+' ')
        f.write(str(d[k])+' ')
        #print d[k]

print c
f.close()


