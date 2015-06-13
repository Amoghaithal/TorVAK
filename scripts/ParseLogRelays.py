from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


relay_info={}
relay_usage_info={}
header=['Virt-time','int-seconds','recv-bytes','send-bytes','cpu-perc','delay-count','avgdelay-millisecs']
with open('shadow.log', 'rw') as inF:
    for line in inF:
        relay=line.split()[4];
        send = ""
        recv = ""
        if("[node]" in line):
            cur_list=[]
            cur_list.append(line.split()[2])
            cur_list.append(re.split(" |;", line)[8].split(',')[0])
            recv = re.split(" |;", line)[8].split(',')[1]
            cur_list.append(recv)
            send = re.split(" |;", line)[8].split(',')[2]
            cur_list.append(send)
            cur_list.append(re.split(" |;", line)[8].split(',')[3])
            cur_list.append(re.split(" |;", line)[8].split(',')[4])
            cur_list.append(re.split(" |;", line)[8].split(',')[5])
            if(relay_info.has_key(relay)):
                relay_info[relay].append(cur_list)
            else:
                relay_info[relay]=list()
                relay_info[relay].append(header)
                relay_info[relay].append(cur_list)
                
            if(relay_usage_info.has_key(relay)):
                relay_usage_info[relay]["send"] +=float(send)
                relay_usage_info[relay]["recv"] +=float(recv)
            else:
                relay_usage_info[relay]=dict()
                relay_usage_info[relay]["relayname"] = relay
                relay_usage_info[relay]["send"] = int(send)
                relay_usage_info[relay]["recv"] = int(recv)
            
            

import csv
for key in relay_info:
    with open(key.split('~')[0]+'.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(relay_info[key])
        print key
with open('relayusage.csv', 'w') as fp:    
    a = csv.writer(fp, delimiter=',')
    a.writerows([["relayname","send","recv"]])
    for key in relay_usage_info: 
        a.writerows([[relay_usage_info[key]["relayname"],relay_usage_info[key]["send"],relay_usage_info[key]["recv"]]])
