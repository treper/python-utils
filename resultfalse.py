import os

f=open("newfilenames.txt","r")
d={}
ff=open("positive_false.txt","r")
fo=open("po.txt","w")
for i in f.readlines():
    i=i.strip("\n")
    l=i.find(" ")
    #print i[]
    d[i[l+1:]]=i[:l]
    
for i in ff.readlines():
    i=i.strip("\n")
    #print i,d[i]
    #print i
    try:
        r=d[i]
        fo.write(r+"\n")
    except:
        continue

f.close()
ff.close()
fo.close()