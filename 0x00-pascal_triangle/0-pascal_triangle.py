#!/usr/bin/python3
list=[1] 
for i in range(10): 
    print(list) 
    newlist=[] 
    newlist.append(list[0]) 
    for i in range(len(list)-1): 
        newlist.append(list[i]+list[i+1]) 
    newlist.append(list[-1]) 
    list=newlist   
