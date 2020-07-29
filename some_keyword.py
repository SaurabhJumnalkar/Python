#Use of Break keyword
lis=[1,2,3,4,5]
for i in  lis:
    print(i)
    if(i==4):
        break

print()
#Use of continue keyword
#To print lis without printing 3
lis=[1,2,3,4,5]
for i in lis:
    if(i==3):
        continue
    print(i)

print()
#use of pass keyword
for i in lis:
    if(i>5):
        pass
    print(i)