#!/bin/python

def rotateByK(arr, k):
  # when k = 0 no rotation
  # needed or gives RecursionError
  if k == 0:
    return arr
 
  n = len(arr)
 
  temp = arr[n - 1]
  for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]
  arr[0] = temp
 
  rotateByK(arr, k - 1)

  return arr


if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8,9]
  k = 3

  print("rotated array: ", rotateByK(arr, k))
  
