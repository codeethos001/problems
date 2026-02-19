#!/bin/python

def duplicates(arr):
  sol = []
  for x in range(len(arr)):
    for y in range(x+1, len(arr)):
      if arr[x] == arr[y] and arr[x] not in sol:
        sol.append(arr[x])

  return sol


if __name__ == "__main__":
  arr = [3,4,5,7,4,2,6,8,9,6,1,3,4]

  print("Duplicate entries: ", duplicates(arr))
