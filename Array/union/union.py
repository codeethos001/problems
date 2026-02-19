#!/bin/python

def union(arr1, arr2):
#  a = len(arr1)
#  b = len(arr2)
#  iterations = (a+b) - ((a-b) if a>=b else (b-a))
#  iterations = a if a>=b else b
  sol = []
#  for x in range(iterations):
#    if arr1[x] in arr2:
#      sol.append(arr1[x])

  if len(arr1) >= len(arr2):
    for x in range(len(arr1)):
      if arr1[x] in arr2:
        sol.append(arr1[x])
  else:
    for x in range(len(arr2)):
      if arr2[x] in arr1:
        sol.append(arr2[x])

# But also one liner possible:
  sol = list(set(arr1) & set(arr2))

  return sol


if __name__ == "__main__":
  arr1 = [1,2,4,5,6,7,8,9]
  arr2 = [4,7,8,11,16]

  print(union(arr1,arr2))
