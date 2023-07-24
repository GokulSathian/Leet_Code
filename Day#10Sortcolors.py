def sort012(list1,n):
  pointer0,pointer2=0,n-1
  list2=[]
  for current in range(len(list1)):
    print(pointer0)
    if list1[current]==0:
      list2.insert(pointer0,0)
      pointer0+=1
    elif list1[current]==2:
      list2.insert(pointer2,2)
      pointer2-=1
    else:
      list2.insert(pointer0,1)
  print(list2)
list1=[2,0,2,1,1,0]
sort012(list1,6)

"""sumary_line
Dutch flag 
three pointer Q 75
"""
