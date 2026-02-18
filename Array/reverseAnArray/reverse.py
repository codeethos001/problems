#!/bin/python

def reverse(arr, size):
  newArr = []
  for i in range(0, size):
#    newArr[i] = arr[size-1-i]
    # array not initialized so we cant use indexing ?
    newArr.append(arr[size-1-i])
    # i = i + 1  is uneccessary for loops python.

  return newArr

def main ():
  arr = [1,2,3,4,5]
  # print(len(arr))

  print (reverse(arr, len(arr)))

if __name__ == "__main__":
  main()
