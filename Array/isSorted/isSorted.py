#!/bin/python
from Array.reverseAnArray.reverse import reverse

def isSorted(arr):
  if len(arr) == 1:
    return True
  for i in range(1, len(arr)):
    if (arr[i-1] > arr[i]):
      return False
  else:
    return True

if __name__ == "__main__":
  arr = [9,8,7,6,5,4,3,2,1]
  revarr = reverse(arr,len(arr))
  if (isSorted(arr)):
    print("True, Sorted in Descending order.")
  elif (isSorted(revarr)):
    print("True, Sorted in Asccending order.")
  else:
    print("False")
