#!/bin/python

def quickSort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  left = [x for x in arr[1:] if x < pivot]
  right = [x for x in arr[1:] if x >= pivot]
  return quickSort(left) + [pivot] + quickSort(right)

def main ():
  arr = [1,5,2,6,9,7,8,4,0]

  arr = quickSort(arr)
  
  print("Max element: " , arr[len(arr)-1])
  print("Min element: " , arr[0])

if __name__ == "__main__":
  main()
