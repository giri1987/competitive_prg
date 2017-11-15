# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:57:25 2017

@author: gpillai082916
"""

vals=map(int,raw_input().split())
def swap(l,r):
 global vals
 tmp=vals[l]
 vals[l]=vals[r]
 vals[r]=tmp    

def partition(l,r):
 global vals
 print(vals)   
 pivot=vals[l]
 j=l
 for i in range((l+1),r+1):
  if vals[i] <= pivot:
   j=j+1
   swap(i,j) 
 swap(l,j)
 return j 
       
def quickSort(l,r):
 if l>=r:
  return
 m=partition(l,r)
 print("m:",m)
 quickSort(l,m-1)
 quickSort((m+1),r)
 
 
def main():
 global vals   
 quickSort(0,len(vals)-1)
 print(vals)

main()   
    
