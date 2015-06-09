'''
Created on 08-Jun-2015

@author: aithal
'''
from tempfile import mkstemp
from shutil import move
from os import remove, close

pat=["VKA:Modified algorithm","VKA:Default algorithm"]
threads={}
with open('shadow.log', 'rw') as inF:
    for line in inF:
        thread_no=line.split()[1]
        if("for the client" in line):
            print_line=""
            cnt=1;
            for l in threads[thread_no]:
                if(l.split().__len__()==9):
                    if((pat[0] in l or pat[1] in l)):
                        print_line+=l.split()[6]+" "
                    elif(l.split()[7].isdigit()):
                        print_line+=l.split()[2]+":"+l.split()[8]+", "                    
            del threads[thread_no]
            client=line.split()[9]
            with open(client, 'a') as outF:
                outF.write(print_line+"\n")            
        else:
            if threads.has_key(thread_no):             
                threads[thread_no].append(line)
            else:
                threads[thread_no] = [line]
                
            
          