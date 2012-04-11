import os,sys,glob,time
from subprocess import Popen, PIPE
dest=" is_admin@10.25.13.154:/home/is_admin/videos/negative/"
while(True):
    l=glob.glob("*.f4v")
    for i in l:
        p1 = Popen(['fuser',i], stdout=PIPE)
        if p1.communicate()[0]=='':
            cmd="scp "+i+dest
            os.system(cmd)
            cmd="rm -f "+i
            os.system(cmd)
    
    time.sleep(60)
        
