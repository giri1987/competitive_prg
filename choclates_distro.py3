def main():
 n=int(input())
 cnt=1
 sm=0
 flag=True
 arr=[]
 del_flg=True

 while flag:
  arr.append(cnt)
  sm=sum(arr)
  if sm > n:
   while del_flg:
    del arr[len(arr)-1]
    sm=sum(arr)
    diff=(n-sm)
    l=len(arr)-1
    if arr[l] < diff:
     del_flg=False
     arr.append(diff)
     break
    if arr[l]>=diff:
     del_flg=False  
     last=arr[l]
     del arr[l]
     arr.append(diff+last)
     break
  #print(del_flg)
  #print(cnt)
  if not del_flg:
   print (len(arr))
   st=' '    
   for i in range(0,len(arr)):
    st=st+' '+str(arr[i])
   print (st.strip())       
   break
      
  cnt+=1
  
main()  