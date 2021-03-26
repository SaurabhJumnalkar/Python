#list declaration
mylist=[1,2,3,4]
print(mylist)
#To concat lists
mylist2=[5,6,7,8]
mylist2.append(mylist)
print(mylist2)

#To insert element in List
mylist.insert(3,5)
print(mylist)

#To delete certaion element from list
mylist.pop(3)
print(mylist)

#To sort list in ascending order
mylist3=[8,1,6,4]
mylist3.sort()
print(mylist3)

#To sort list in discending order
mylist3.reverse()
print(mylist3)

#to find smallest element in list
print(min(mylist3))

#to find biggest element in list
print(max(mylist3))
