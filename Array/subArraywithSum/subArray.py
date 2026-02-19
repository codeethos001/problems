#!/bin/python

def subArray(arr, target):
  n = len(arr)
#  sum0 = 0

  for i in range(n):
    sum0 = 0
    for j in range(i, n):
      sum0 += arr[j]
      if sum0 == target:
        return arr[i:j+1]

  return None


if __name__ == "__main__":
  arr = [1,2,3,7,5,6,0]
  target = 12 
  print("Sub array:", subArray(arr, target))

