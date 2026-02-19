#!/bin/python

# print arr[j] - arr[i] when j > i ?

def maxDiff(arr):

  minIndex = arr[0]
  maxDiff = arr[1] - arr[0]

  for i in range(1, len(arr)):
    if arr[i] - minIndex > maxDiff:
      maxDiff = arr[i] - minIndex

    if arr[i] < minIndex:
      minIndex = arr[i]

  return maxDiff


if __name__ == "__main__":
  arr = [2,3,10,6,4,8,1]
  print("Max Difference:", maxDiff(arr))

