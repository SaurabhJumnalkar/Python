#args
def sum(*num):
    print(num)
sum(1,2,3,4,5,6,7)

#kwargs
def sum2(**num):
    print(num)
sum2(name="Best",year="2000",month="july")

#combination of both
def sum3(num,*num1,**num2):
    print(num)
    print(num1)
    print(num2)
sum3(1,2,3,4,5,6,key="password",year="1947",place="India")