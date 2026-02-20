#!/bin/python

"""
Find the Longest Consecutive Sequence: 
Find the length of the longest consecutive sequence of integers.
"""

def longestConsecutive(arr):
  longest = 0

  for i in range(len(arr)):

    current = arr[i]
    length = 1

    while True:
      got = False

      for j in range(len(arr)):
        if arr[j] == current + 1:
          current += 1
          length += 1
          got = True
          break

      if not got:
        break
    print(length)

    if length > longest:
      longest = length

#  print(longest)

  return lognest

if __name__ == "__main__":
  arr = [10,4,20,1,3,2]
  print("Longest consecutive length:", longestConsecutive(arr))

