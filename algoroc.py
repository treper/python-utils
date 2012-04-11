import os,sys,glob,re
if __name__=="__main__":
    pf=open("positiveset.txt","r")
    l=[]
    for i in pf.readlines():
        it=i.strip("\n")
        l.append(it)
        
    pf.close()
    rf=open("positive_result_to_choose.txt","r")
    c=0
    t=0
    for i in rf.readlines():
        it=i.strip("\n")
        t=t+1
        if it in l:
            c=c+1
    
    rf.close()
    print "FNR=",(1-float(c)/float(t))*100
    rf=open("")