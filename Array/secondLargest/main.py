#!/bin/python
from Array.findMaxMin.maxMin import quickSort
from Array import array

def secondLargest(arr):
  arr = quickSort(arr)
  return arr[len(arr)-2]

def main():
  print(array)
  print("Second Largest Element: ",secondLargest(array))

if __name__ == "__main__":
  main()
