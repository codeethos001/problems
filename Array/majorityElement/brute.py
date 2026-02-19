#!/bin/python

# Find Majority Element: Find the element that appears more than n/2 times.

def majorityElement(arr):
  n = len(arr)

  for i in range(n):
    count = 0
    for j in range(n):
      if arr[j] == arr[i]:
        count += 1

    if count > n // 2:
      return arr[i]

  return None


if __name__ == "__main__":
  arr1 = [1,3,5,8,4,4,6,7,8,3,4,6,8,9,0,4,8,3,2,4,3,6,8]
  arr = [4,4,4,2,4,3,4,4,1,4,4,5,4]

  print("Majority Elemen: ", majorityElement(arr))
  
