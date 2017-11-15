# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:11:13 2017

@author: gpillai082916
"""

n=int(raw_input())
val=map(int,raw_input().split())
#print(val)
#
dict={}   
for i in val:
 if i in dict.keys():
   dict[i]=dict[i]+1
 else:
   dict[i]=1

tups=sorted(dict.items(),key=lambda (k,v):(v,k))

for i in tups:
    if i[1] > (n/2):
        print(1)
        break

        
     
    
   
   
     

