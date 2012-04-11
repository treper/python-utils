from hash_ring import *
memcache_servers = ['127.0.0.1','10.25.13.152','10.25.13.154']
ring = HashRing(memcache_servers)
f=open("keyslist-all.txt","r")
fo=open("distrikeys.txt","w")
d={}
for i in memcache_servers:
    d[i]=0
    
for i in f.readlines():
    itemId=i.strip("\n")
    server = ring.get_node(itemId)
    d[server]=d[server]+1
    #print server
    fo.write(itemId+" "+server+"\n")
f.close()
fo.close()

for i in memcache_servers:
    print d[i]
    