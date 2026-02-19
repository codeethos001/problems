#!/bin/python

# max product Pair therefore the largest numbers will make the max product.

def maxProduct(arr):
  n = len(arr)

  if n < 2:
    return None

  arr.sort()
  return (arr[n-1], arr[n-2])


if __name__ == "__main__":
  arr = [1,4,3,6,7,2]
  print("Max product", maxProduct(arr))

