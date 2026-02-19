#!/bin/python

def subArrays(arr):
  n = len(arr)
  sol = []

  for i in range(n):
    for j in range(i, n):
      sol.append(arr[i:j+1])

  return sol

if __name__ == "__main__":
  arr = [1,2,3,4,5,6]
  
  print("Subarrays:")
  for x in subArrays(arr):
    print (x)
