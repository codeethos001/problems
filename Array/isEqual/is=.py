#!/bin/python

def isEqual(arr1, arr2):
  check = 0
  if len(arr1) == len(arr2):
    for x in range(len(arr1)):
      if arr1[x] == arr2[x]:
        check += 1
  else:
    return False
  if check == len(arr1):
    return True


if __name__ == "__main__":
  arr1 = [1,2,3,4,5,6,7]
  arr2 = [2,3,1,7,5,4,6]

  if isEqual(sorted(arr1),sorted(arr2)):
    print("True")
  else:
    print("False")
