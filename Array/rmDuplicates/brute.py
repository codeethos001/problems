#!/bin/python

# Very bad time and space complexity

def rmDuplicate(arr):
  dupIndex = []
  for x in range(len(arr)):
    for y in range(x+1, len(arr)):
      if arr[x] == arr[y]:
#        print("Found duplicate")
        dupIndex.append(y)
  
  for i in dupIndex:
    del(arr[i])
        
  return arr

if __name__ == "__main__":
  arr = [6,2,5,9,4,3,5,8,2]
  # Expected sol for test - 2 loops of found duplicate
  print("Removed Duplicates: ",rmDuplicate(arr))
