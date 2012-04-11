import os,sys
from subprocess import Popen, PIPE
if __name__=="__main__":
    argv=sys.argv
    totalkeyslst=argv[1]
    print totalkeyslst
    slavelst=argv[2]
    print slavelst
    sl=open(slavelst,"r")
    ips=[]
    smap=[]
    alkmap=[]
    totalmem=0
    ts=0
    for i in sl.readlines():
        line=i.strip("\n")
        ip,mem=line.split(" ")
        ips.append(ip)
        smap.append(mem)
        totalmem=totalmem+int(mem)
        ts=ts+1
    
    tk=len(open(totalkeyslst,"r").readlines())  
    tmp=0
    for i in range(ts):
        t=int(tk*int(smap[i])/totalmem)
        alkmap.append(t)
        tmp=tmp+t
        #print smap[i],alkmap[i]
    
    alkmap[i]=tk-tmp+t

    for i in alkmap:
        print i
    onlst=[]
    d,ext=os.path.splitext(totalkeyslst)
    for i in range(ts):
        onlst.append(d+str(i+1)+ext)
    
    j=0
    ct=0
    for i in range(ts):
        if j==0:
            cmd="head -"+str(alkmap[i])+" "+totalkeyslst+" >"+onlst[j]
        else:
            cmd="head -"+str(ct+alkmap[i])+" "+totalkeyslst+"|tail -"+str(alkmap[i])+" >"+onlst[j]
        os.system(cmd)
        print cmd
        if j==0:
            pass
        else:
            cmd="scp "+onlst[j]+" is_admin@"+ips[j]+":"+totalkeyslst
            os.system(cmd)
        ct=ct+alkmap[i]
        j=j+1

    
    
    
