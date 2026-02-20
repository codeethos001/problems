#!/bin/python

def maxSumSubArray(arr):
  sol = arr[0]

  for i in range(len(arr)):
    sum0 = 0
    for j in range(i, len(arr)):
      sum0 += arr[j]

      if sum0 > sol:
        sol = sum0
    
  return sol

if __name__ == "__main__":
  arr = [1,2,3,4,6,7,8,9]
  arr1 = [2,-9,5,9,0,-1,3,-4,30]
  print(maxSumSubArray(arr1))
