#!/bin/python

def countFreq(arr):

  dictFreq = {}

  for num in arr:
    if num not in arr:
      dictFreq[num] = 0
#    dictFreq[num] += 1
    dictFreq[num] = dictFreq.get(num, 0) + 1

  return dictFreq


if __name__ == "__main__":
  arr = [10, 20, 10, 5, 20]

  sol = countFreq(arr)

  print(sol)
