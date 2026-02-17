#!/bin/python

def sumOfElements (arr):
  sum = 0
  for i in range (0, len(arr)):
    sum = sum + arr[i]

  return sum

def main ():
  arr = [2,3,4,5,6,7,8,9]
  
  print("Sum of elements: ", sumOfElements(arr))

if __name__ == "__main__":
  main()
