import os,sys,re

FFMPEG="ffmpeg"
CODEWAV="/root/tmp/musicretr-2.2.6/codewav"
f=open("video_list.lst","r")
for vn in f.readlines():
    inputfn=vn.strip("\n")
    outputfn=os.path.splitext(vn)[0]+".key"
    cmd = FFMPEG+" -i "+inputfn+" -y  -ar 11025 -ab 128k tmp.wav"
    os.system(cmd)
    #print cmd
    cmd = CODEWAV+" boostextdescr.txt 1 tmp.wav "+outputfn
    #print cmd
    os.system(cmd)
    
f.close()