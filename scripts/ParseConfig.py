'''
Created on 02-Jun-2015

@author: aithal
'''
from tempfile import mkstemp
from shutil import move
from os import remove, close
from Canvas import Line
posclients=[("tgen.torperf5mclient.graphml","5242880"),("tgen.torperf1mclient.graphml","1048576"),("tgen.torperf50kclient.graphml.xml","51200"),("tgen.torbulkclient.graphml","10485760"),("tgen.torwebclient.graphml.xml","10240")]
printline=[]
cnt=0
with open('shadow.config.xml', 'rw') as inF:
    for line in inF:
        for client in posclients:
            if client[0] in line:
                printline[cnt-1]=printline[cnt-1].replace("\"/>"," --Size"+" "+client[1]+"\"/>")
        printline.append(line)
        cnt=cnt+1
with open('shadow1.config.xml','w') as new_file:
    for line in printline:
        new_file.write(line)
