import os,sys,glob,time,json
slavelst=['127.0.0.1','10.25.13.152','10.25.13.153','10.25.13.154']
loadkeydir={}
loadkeydir['VF12']='/home/is_admin/MRPlatform/src/Test/keys/keyslist-all.txt'
testkeydir['VF6']='/home/is_admin/videos/'
loadkeydir['AF']='/home/is_admin/MRPlatform/src/Test/keys/keyslist-all.txt'
method=['VF12','VF6','AF']
min_score=range(5,26)
seg=[100,200,400,600,800,1000,1200,1400,1600]
neighborhood=range(1,3)
f=open("./config/cfg.lst","r")
for i in f.readlines():
    cfg_list.append(i.strip("\n"))
for i in cfg_list:
    #change app config files and switch parameters
    pmaster.stdin.write("")
    #generate
    lt=0
    lr=1
    while(lt!=lr):
        #get the tested keys number from appconfig file i
        json_data = open(i)
        data = json.load()
        loadlist = str(data["KeysLocation"]["LoadKeysList"])
        print loadlist
        #%sms%2.2fseg%dsample%dcutoff%2.2fv%dn%d%s_result.txt
        pon = os.path.basename(str(data["KeysLocation"]["TestKeysList"]))[0:8]
        of=str(data["AlgoParams"]["method"])+"ms"+'%2.2f'%float(str(data["AlgoParams"]["em_min_score"]))+"seg"+str(data["AlgoParams"]["keys_num_a_seg"])+"sample"+str(data["AlgoParams"]["samplingNum"])+"cutoff"+str(data["AlgoParams"]["cutoffpercent"])+"v"+str(data["AlgoParams"]["verifymethodid"])+"n"+str(data["AlgoParams"]["neighbormethodid"])+pon+"_result.txt"
        print of
        pc = Popen("cat "+ loadlist + " |wc -l", stdin = PIPE, stdout = PIPE, stderr = None, shell = True)
        lt = int(pc.stdout.read())
        print lt
        pc = Popen("cat "+ of + " |wc -l", stdin = PIPE, stdout = PIPE, stderr = None, shell = True)
        lr = int(pc.stdout.read())
        print lr
        time.sleep(60)
