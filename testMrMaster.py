import os,sys,glob,time,json
from subprocess import *
pmaster = Popen("./MrMaster", stdin = PIPE, stdout = PIPE, stderr = None, shell = True)
cfg_list=[]
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
    #wait for database queries
    time.sleep(10)
