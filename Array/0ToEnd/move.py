#!/bin/python

def move0ToEnd(arr):
  n = len(arr) - 1
  zeros = []
  
  for i in range(n, -1, -1): # Backward iterate
    if arr[i] == 0:
      del arr[i]
      zeros.append(0)
  
  return arr + zeros

if __name__ == "__main__":
  arr1 = [6,2,4,0,6,0,1,3,0,1,3,7,0,6,4,0,2,0,9,0]

  print("Zeros in the end:", move0ToEnd(arr1))

