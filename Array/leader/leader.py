#!/bin/python

# Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def leaders(arr):
  n = len(arr)
  sol = []

  for i in range(n):
    isLeader = True
    for j in range(i + 1, n):
      if arr[j] > arr[i]:
        isLeader = False
        break

    if isLeader:
      sol.append(arr[i])

  return sol

if __name__ == "__main__":
  arr1 = [5,2,4,6,2,8,9,0]

  print("Leader: ", leaders(arr1))
