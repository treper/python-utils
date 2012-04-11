import os
import os.path

dir="E:/positive"
p=[]
fo=open("newfilenames.txt","w")
for pa,dn,fn in os.walk(dir):
    #p.append(pa)
    #print pa,fn
    #r=pa.find(" ")
    #print pa,pa[:20]
    #shutil.move(pa,pa[:20])
    #itemid=pa[12:r]
    #print itemid
    count=0
    for i in fn:
        #print fn
        name,ext=os.path.splitext(i);
        #print name,ext
        #rename the filenames
        newfilename='188'+'0'*(6-len(str(count)))+str(count)
        fo.write(name+" "+newfilename+"\n")
        print os.path.join(pa,i),os.path.join(pa,newfilename+ext)
        os.rename(os.path.join(pa,i),os.path.join(pa,newfilename+ext))
        count=count+1

fo.close()
