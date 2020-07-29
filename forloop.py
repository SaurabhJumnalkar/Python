#for loop
#To print loop runs how many times
for i in range(7):      #here i is initialized, for loop is executed in range of 7 means till i becomes 7 and here doen't need for i++
    print("loop runs",i,"times.")

#To print Elements in a list
lis=[1,2,3,"hi","How","Are","You?"]
for i in lis:
    print(i)

#To print characters in a String
Str="HELLO"
for i in Str:
    print(i)

#To print nos. in specific range
for i in range(2,7):
    print(i)

#To print NOs. in interval of 2
for i in range(2,7,2):
    print(i)

#small program nested loop
for i in range(7):
    print("outer loop runs for ",i,"times")
    for j in range(3):
        print("Inner loop runs",j,"times & in",i,"th Outer loop") 