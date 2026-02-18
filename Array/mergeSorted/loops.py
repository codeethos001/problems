#!/bin/python

from Array.findMaxMin.maxMin import quickSort

def mergeSorted(sArr1, sArr2):
#  n = len(sArr1) + len(sArr2)
  sol = []
  for x in range(len(sArr1)):
    for y in range(len(sArr2)):
      if sArr1[x] <= sArr2[y]:
        sol[x] = sArr1[x]
        sol[x+1] = sArr2[y]
      else:
        sol[x] = sArr2[y]
        sol[x+1] = sArr1[x]

  return sol

if __name__ == "__main__":
  sArr1 = [7,3,9,1,5]
  sArr2 = [2,4,4,6,0]
  sArr1 = quickSort(sArr1)
  sArr2 = quickSort(sArr2)

  print("Solution: ", mergeSorted(sArr1,sArr2))

