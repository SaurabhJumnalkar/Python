#unordered collection having unique elements is set.
#Declaration of set
set1={1,2,3,4,7,8}
print(set1)

#union of two sets
set2={6,8,7,10,9}
print(set1|set2)
print(set1.union(set2)) # another way

#intersection of set
print(set1 & set2)
print(set1.intersection(set2)) #another way

#to add elements in set
set1.add(11)   # single element
print(set1)
set1.update([12,13,14])  #multiple elements
print(set1)

#To find length of set
print(len(set1))

#To remove elements from set
set1.remove(11)  # specific
print(set1)
print(set1.pop())  # random
print(set1)
set1.clear()
print(set1)  #to remove all