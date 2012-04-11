import os,sys,re,string

f=open("newfilenamesnew.txt","r")
fr=open("positive_results.txt","r")

d={}
for i in f.readlines():
    i=i.strip("\n")
    m,n=i.split(" ")
    p=string.atoi(m)
    q=string.atoi(n)
    d[p]=q

f.close()
count=0
for j in fr.readlines():
    j=j.strip("\n")
    m,n=j.split(" ")
    p=string.atoi(m)
    q=string.atoi(n)
    try:
        print d[p],q
        if d[p]/10==q:
            count=count+1
    except:
        pass

fr.close()
print count
    