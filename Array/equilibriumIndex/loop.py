#!/bin/python

def equilibriumIndex(arr):
  n = len(arr)

  for i in range(n):
    leftSum = 0
    rightSum = 0

    # sum of left side
    for j in range(0, i):
      leftSum += arr[j]

    # sum of right side
    for j in range(i+1, n):
      rightSum += arr[j]

    if leftSum == rightSum:
      return i

if __name__ == "__main__":
  arr = [-7,1,5,2,-4,3,0]
  print("equilibrium index:", equilibriumIndex(arr), 
        "\nArray element: ", arr[equilibriumIndex(arr)])

