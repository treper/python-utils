import os,shutil
import os.path

dir="E:/positive"
p=[]
for pa,dn,fn in os.walk(dir):
    #p.append(pa)
    #print pa
    #r=pa.find(" ")
    #print pa,pa[:20]
    #shutil.move(pa,pa[:20])
    #itemid=pa[12:]
    #print itemid
    #count=0
    for i in fn:
        #name,ext=os.path.splitext(i);
        #print name,ext
        #rename the filenames
        #print os.path.join(pa,i),os.path.join(pa,itemid+str(count)+ext)
        #os.rename(os.path.join(pa,i),os.path.join(pa,itemid+str(count)+ext))
        shutil.move(os.path.join(pa,i),os.path.join(dir,i))
        #count=count+1

#for i in p:
    #os.rename(i,i[:20])