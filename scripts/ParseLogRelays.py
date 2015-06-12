from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


relay_info={}
Header=[['Virt-time','int-seconds','recv-bytes','send-bytes','cpu-perc','delay-count','avgdelay-millisecs']]
with open('shadow.log', 'rw') as inF:
    for line in inF:
        relay=line.split()[4];
        if("[node]" in line):
            cur_list=[]
            cur_list.append(line.split()[2])
            cur_list.append(re.split(" |;", line)[8].split(',')[0])
            cur_list.append(re.split(" |;", line)[8].split(',')[1])
            cur_list.append(re.split(" |;", line)[8].split(',')[2])
            cur_list.append(re.split(" |;", line)[8].split(',')[3])
            cur_list.append(re.split(" |;", line)[8].split(',')[4])
            cur_list.append(re.split(" |;", line)[8].split(',')[5])
            if(relay_info.has_key(relay)):
                relay_info[relay].append(cur_list)
            else:
                relay_info[relay]=Header
                relay_info[relay].append(cur_list)

import csv
for key in relay_info:
    with open(key.split('~')[0]+'.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(relay_info[key])
        print key