#!/bin/python

def sort012(arr):
  zeros = []
  ones = []
  twos = []

  for x in arr:
    if x == 0:
      zeros.append(x)
    elif x == 1:
      ones.append(x)
    else:
      twos.append(x)

  return zeros + ones + twos

if __name__ == "__main__":
  arr = [2,0,2,1,1,0]
  print("Sorted:", sort012(arr))
