#!/bin/python

def findPeak(arr):
  left = 0
  right = len(arr) - 1

  while left < right:
    mid = (left + right) // 2

    if arr[mid] < arr[mid+1]:
      left = mid + 1
    else:
      right = mid

  return arr[left]


if __name__ == "__main__":
  arr = [1,2,20,4,3,0]
  print("Peak: ", findPeak(arr))

