#!/bin/python

def productExceptSelf(arr):
  n = len(arr)
  sol = []

  for i in range(n):
    prod = 1

    for j in range(n):
      if i != j:
        prod *= arr[j]

    sol.append(prod)

  return sol


if __name__ == "__main__":
  arr = [1,2,3,4]
  print(productExceptSelf(arr))

