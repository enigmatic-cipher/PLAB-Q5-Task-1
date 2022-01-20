"""
Given a List as input. Create a new List in which each element is multiplied by 10. Print this new List.
Input-> [1,3,4,7]
Output->
10
30
40
70
"""

lst = [1,3,4,7]
ln = len(lst)
for i in range(0,ln):
  e = lst[i]
  print(e*10)
