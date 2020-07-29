#program to find greatest number among three nos.
a=input()
b=input()
c=input()
if (a>b):
    if (a>c):
        print("{} is greatest".format(a))
    else:
        print("{} is greatest".format(c))
else:
    if (b>c):
        print("{} is greatest".format(b))
    else:
        print("{} is greatest".format(c))    
    