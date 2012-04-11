import os,sys,glob,time
from subprocess import Popen, PIPE

FFMPEG="/home/is_admin/lab/codevideo-current/ffmpeg_logo_116_0831"
CODEVIDEO="/home/is_admin/lab/codevideo/codevideo.exe"
CODEWAV="/home/is_admin/lab/musicretr-2.2.6/codewav"
KEYSGENDIR="/home/is_admin/videos/negative-keys/"
WAVSGENDIR="/home/is_admin/videos/negative-wavs/"

l=[]
if os.path.exists("generated.txt"):
    pass
else:
    fr=open("generated.txt","r")
    for fn in fr.readlines():
        itemId =fn.strip("\n")
        l.append(itemId)
    fr.close()
f=open("generated.txt","a")
while(True):
    ln=glob.glob("*.f4v")
    for i in ln:
        if i not in l:
            p1 = Popen(['./fuser',i], stdout=PIPE)
            if p1.communicate()[0]=='':
                outputfn=KEYSGENDIR+i[0:-4]+".key"
                if os.path.exists(outputfn):
                    pass
                else:
                    cmd=FFMPEG+" -i "+i+" -y -r 6 -s 160x120  -qscale 10 -an tmp.flv"
                    os.system(cmd)
                    cmd = CODEVIDEO+" tmp.flv "+outputfn
                    os.system(cmd)
		outputfn=WAVSGENDIR+i[0:-4]+".key"
		if os.path.exists(outputfn):
                    pass
                else:
		    cmd=FFMPEG+" -i "+i+" -y  -ar 11025 -ab 128k tmp.wav"
		    os.system(cmd)
		    cmd=CODEWAV+" boostdescr3.txt 1 tmp.wav "+outputfn
		    os.system(cmd)
                f.write(i+"\n")
        	l.append(i)
    time.sleep(10)
f.close()
