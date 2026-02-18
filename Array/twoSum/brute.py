#!/bin/python

def twoSum(arr, target):

  sol = [
      ]
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == target:
        sol.append([arr[i], arr[j]])
#        print (arr[i], arr[j])
  return sol


if __name__ == "__main__":
  arr = [2,4,-6,8,-3,7,5]
  target = -9
  for x in twoSum(arr,target):
    print(x)

