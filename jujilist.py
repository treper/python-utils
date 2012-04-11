import re,urllib
f=open("id-title.txt","rb")
fo=open("juji.lst","w")
pr=re.compile("[\u2e80-\uffff]+\d\d")
for i in f.readlines():
    l=i.find(" ")
    k=i[:l]
    title = i[l:]
    ma=re.findall(pr,title)
    if ma and len(title)<10:
        #print title
        fo.write(k+" "+title+"\n")

f.close()
fo.close()