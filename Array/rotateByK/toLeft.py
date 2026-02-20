#!/bin/python

def rotateByK(arr, k):
  if k == 0:
    return arr

  n = len(arr)
  temp = arr[0]

  for i in range(0, n-1):
    arr[i] = arr[i+1]

  arr[n-1] = temp
  rotateByK(arr, k - 1)

  return arr

if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8,9]
  k = 5

  print("rotated array: ", rotateByK(arr, k))

