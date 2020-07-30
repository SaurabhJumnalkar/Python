#factorial by recursion
def fact(x):
    if(x==0):
        return 1
    else:
        result=x*fact(x-1)
    return result
print(fact(10))

#sumof 20 to 1 nos.
def add(x):
    if(x==1):
        return 1
    else:
        sum=x+add(x-1)
    return sum

print(add(20))