# Given three Sorted arrays in non-decreasing order, print all common elements in these arrays.

# Examples: 

# Input: 
# ar1[] = {1, 5, 10, 20, 40, 80} 
# ar2[] = {6, 7, 20, 80, 100} 
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
# Output: 20, 80

# Input: 
# ar1[] = {1, 5, 5} 
# ar2[] = {3, 4, 5, 5, 10} 
# ar3[] = {5, 5, 10, 20} 
# Output: 5, 5

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)


def findCommon(ar1, ar2, ar3, n1, n2, n3):
  i, j, k = 0, 0, 0
  while (i < n1 and j < n2 and k < n3):
    if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
      print (ar1[i])
      i += 1
      j += 1
      k += 1
 
        # x < y
    elif ar1[i] < ar2[j]:
      i += 1
 
        # y < z
    elif ar2[j] < ar3[k]:
      j += 1
 
        # We reach here when x > y and z < y, i.e., z is smallest
    else:
      k += 1


print ("Common elements are")
findCommon(ar1, ar2, ar3, n1, n2, n3)
