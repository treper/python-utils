import re,mechanize,elixir,sqlalchemy
br=mechanize.Browser()
br.set_handle_robots(False)
em=re.compile(r"[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}",re.IGNORECASE)
dbf=open("emdb.txt","rb")
dblist=[]
for n in dbf.readlines():
    dblist.append(n.strip("\n"))

dbf.close()
dbf=open("emdb.txt","a")
mlist=[]
#print "baidu"
baiduurl=["http://zhidao.baidu.com/q?ct=17&tn=ikaslist&rn=10&word=%C7%F3%20pdf&lm=65536&pn=","http://zhidao.baidu.com/q?ct=17&tn=ikaslist&rn=10&word=%C7%F3%B9%BA%20pdf&lm=65536&pn=","http://zhidao.baidu.com/q?ct=17&lm=65536&tn=ikaslist&rn=10&word=%C7%F3%20%B5%E7%D7%D3%B0%E6&pn=","http://zhidao.baidu.com/q?ct=17&lm=65536&tn=ikaslist&pn=0&rn=10&word=%C7%F3%B9%BA%20%CA%E9","http://zhidao.baidu.com/q?ct=17&lm=65536&tn=ikaslist&pn=0&rn=10&word=%C7%F3%20%BD%CC%B2%C4","http://zhidao.baidu.com/q?ct=17&lm=65536&tn=ikaslist&pn=0&rn=10&word=%C7%F3%20%CA%E9%BC%AE","http://zhidao.baidu.com/q?ct=17&lm=65536&tn=ikaslist&pn=0&rn=10&word=%C7%F3%20%CA%E9%B1%BE"]
for j in baiduurl:
    for i in range(20):
        #print i
        url=j+str(i*10)
        rp=br.open(url)
        ct=rp.read()
        ma=re.findall(em,ct)
        if ma:
            for k in ma:
                if k not in dblist and k not in mlist:
                    print k+";"
                    mlist.append(k)
                    dbf.write(k+"\n")  
#print "soso"
sosourl=["http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+pdf&st=1&sci=0&pg=","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+%E7%94%B5%E5%AD%90%E7%89%88&st=1&sci=0&pg=","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+%E7%94%B5%E5%AD%90%E4%B9%A6&st=1&sci=0&pg=","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+%E6%95%99%E6%9D%90&st=1&sci=0&pg=","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+%E8%80%83%E7%A0%94&st=1&sci=0&pg=","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82+%E4%B9%A6%E7%B1%8D&st=1&sci=0&pg="]
for j in sosourl:
    for i in range(12):
        #print i
        url=j+str(i)
        try:
            rp=br.open(url)
        except:
            break
        ct=rp.read()
        ma=re.findall(em,ct)
        if ma:
            for k in ma:
                if k not in dblist and k not in mlist:
                    print k+";"
                    mlist.append(k)
                    dbf.write(k+"\n")  
#print "etao"
etaourl=["http://q.etao.com/searched_buy_threads.htm?q=%B5%E7%D7%D3%B0%E6","http://q.etao.com/searched_buy_threads.htm?q=%B5%E7%D7%D3%CA%E9","http://q.etao.com/searched_buy_threads.htm?q=%C7%F3%CA%E9","http://q.etao.com/searched_buy_threads.htm?q=pdf","http://q.etao.com/searched_buy_threads.htm?q=%BD%CC%B2%C4","http://q.etao.com/searched_buy_threads.htm?q=%BF%BC%D1%D0","http://q.etao.com/searched_buy_threads.htm?q=%BF%CE%B1%BE","http://q.etao.com/searched_buy_threads.htm?q=%BD%CC%B3%CC","http://wenwen.soso.com/z/Search.e?sp=S%E6%B1%82%E8%B4%AD+%E7%94%B5%E5%AD%90%E7%89%88&st=1&sci=0&pid=w.search.djj"]
for j in etaourl:
    try:
        rp=br.open(j)
    except:
        break
    ct=rp.read()
    ma=re.findall(em,ct)
    if ma:
        for k in ma:
            if k not in dblist and k not in mlist:
                print k+";"
                mlist.append(k)
                dbf.write(k+"\n")  

#for i in mlist:
    #dbf.write(i+"\n")    
dbf.close()
    
    
    
    
