a = [3, 4, 2, 5, 7, 9, 7, 5, 6, 32, 54, 66, 78, 12, 62, 45, 23, 32, 21, 54, 89]
# use append for added a data in the last position
a.append(102)
print(a)
# use insert, has two parameter (postion, value)
a.insert(1, 20)
print(a)

# use remove , u can remove data from any here , only u have use vlue
a.remove(102)
print(a)
# use pop, its means also delete data from last of the list
a.pop()
print(a)

# use clear , delete all data from the list
""" a.clear()
print(a) """

# sort
a.sort()
print(a)

# reverse
a.reverse()
print(a)

# copy
b = a.copy()
b.reverse()
print(b)
