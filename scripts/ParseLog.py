'''
Created on 08-Jun-2015

@author: aithal
'''
from tempfile import mkstemp
from shutil import move
from os import remove, close
import sys

pat=["VKA:Fast Circuit"," VKA:Normal circuit"]
threads={}
entry_guards={}
middle_guards={}
exit_guards={}
total_relays={}
digests={}
def add(dict,client,relay):
    relay_name=relay
    if(digests.has_key(relay)):
        relay_name=digests[relay]
    if(dict.has_key(client)):
        if(relay_name not in dict[client]):
            dict[client].append(relay_name)
    else:
        dict[client]=list()
        dict[client].append(relay_name)
def main(argv):
    with open(argv[1],'r') as inF:
        cnt=1
        for line in inF:
            if(cnt==1):
                cnt+=1
                continue
            else:
                digests[line.split()[0].split("=$")[1]]=line.split()[2].split("=")[1]
                cnt+=1
    with open(argv[0], 'rw') as inF:
        for line in inF:
            thread_no=line.split()[1]
            if("for the client" in line):
                print_line=""
                cnt=1;
                for l in threads[thread_no]:
                    if((pat[0] in l or pat[1] in l)):
                        print_line+=l.split()[6]+" "
                    elif(l.split().__len__()==9 and l.split()[7].isdigit()):
                        print_line+=l.split()[2]+":"+l.split()[8]+", "
                        if(int(l.split()[6])!=1):
                            add(total_relays,line.split()[9],l.split()[8])
                            if( int(l.split()[6])==3):
                                if(int(l.split()[7])==1):
                                    add(entry_guards,line.split()[9],l.split()[8])
                                elif(int(l.split()[7])==2):
                                    add(middle_guards,line.split()[9],l.split()[8])
                                else:
                                    add(exit_guards,line.split()[9],l.split()[8])
                del threads[thread_no]
                client=line.split()[9]
                with open(client, 'a') as outF:
                    outF.write(print_line+"\n")            
            else:
                if threads.has_key(thread_no):             
                    threads[thread_no].append(line)
                else:
                    threads[thread_no] = [line]

if __name__ == "__main__":
   main(sys.argv[1:])  
   
import csv
with open("RelayCount"+'.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows([["Client","Entry_num","Middle_num","Exit_num","Total_num"]])    
    for key in total_relays:
        a.writerows([[key,entry_guards[key].__len__(),middle_guards[key].__len__(),exit_guards[key].__len__(),total_relays[key].__len__()]])
                
          
  