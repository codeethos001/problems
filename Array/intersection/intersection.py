#!/bin/python

def intersection(arr1,arr2):
  sol = []
  for x in arr1:
    if x in arr2 and x not in sol:
      sol.append(x)

  return sol

if __name__ == "__main__":
  arr1 = [4,5,2,5,9,0,1]
  arr2 = [1,2,3,4,5]

  print("Same elements: ", intersection(arr1, arr2))
