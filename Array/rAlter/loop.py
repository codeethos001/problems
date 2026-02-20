#!/bin/python

def rearrange(arr):
  arr.sort()
  sol = []

  while arr:
    sol.append(arr.pop())
    if arr:
      sol.append(arr.pop(0))

  return sol

if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8]
  print("Rearrange Alternately: ", rearrange(arr))

