#!/bin/python
#from Array.findMaxMin.maxMin import quickSort

def missing(arr, n):
  # here n is the limit.
  sol = []
  for i in range(n):
    if i not in arr:
      sol.append(i)
  
  return sol

if __name__ == "__main__":
  arr = [1,5,8,9,2,0,4,10,12,14]
  target = 15

#  arr = quickSort(arr)
  print("Missing Elements: ", missing(arr,target))
