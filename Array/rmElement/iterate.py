#!/bin/python
from Array.reverseAnArray.reverse import reverse

def rmElement(arr, target):
  toRemove = []
  for i in range(len(arr)):
    if arr[i] == target:
      toRemove.append(i)
  
#  for x in toRemove: # Bug changes indices when removed.
  for x in reverse(toRemove, len(toRemove)): # So i del from last index.
    del(arr[x])

  return arr

if __name__ == "__main__":
  arr = [3,4,6,1,4,6,9,0]
  target = 6

  print("Removed", target, "from array: ", rmElement(arr,target))

