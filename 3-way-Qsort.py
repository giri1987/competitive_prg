# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:57:25 2017

@author: gpillai082916
"""
n=int(raw_input())
vals=map(int,raw_input().split())
def swap(l,r):
 global vals
 tmp=vals[l]
 vals[l]=vals[r]
 vals[r]=tmp    

#3-way partitioning

def partition3(l,r):
 global vals
 dup=vals[l:r]
 #print(dup)
 
 #print("l,r :",(l,r))
 mid=len(dup)/2
 
 #print("mid_pos: ", mid)
 m_val=dup[mid]
 #print("mid_value:",m_val)
 m_arr=[]
 l_arr=[]
 r_arr=[]
 
 for i in dup:
  if i == m_val :
   m_arr.append(i)
  elif i<m_val:
   l_arr.append(i)
  else:
   r_arr.append(i)
 
 vals[l:r]=l_arr+m_arr+r_arr
 #print("vals :",vals)
 m1=l+len(l_arr)
 if m1 < 0 :
     m1=0
  
 m2=m1+(len(m_arr))
 if m2 < 0:
     m2=r
 return (m1,m2)

#Regular Partitioning
def partition(l,r):
 global vals
 #print(vals)   
 pivot=vals[l]
 j=l
 
 #for i in range((l+1),r+1):
 #Note : As we are calling as upper bound : r which is already (n+1).
 
 for i in range((l+1),r): 
  if vals[i] <= pivot:
   j=j+1
   swap(i,j) 
 swap(l,j)
 return j 

#Regular quick sort
#==================
       
def quickSort(l,r):
 if l>=r:
  return
 m=partition(l,r)
 #print("m:",m)
 quickSort(l,m-1)
 quickSort((m+1),r)

#3-way quickSort
#===============
def quickSort3(l,r):
 if l>=r:
     return
 (m1,m2)=partition3(l,r)
 #print("m's :",(m1,m2))
 quickSort3(l,m1)
 quickSort3(m2,r) 
 
def main():
 global vals   
 quickSort3(0,len(vals))
 #print(vals)

main()   
    



