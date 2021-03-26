#To define and call function 
def funaname():
    print("Hello")
    print("You are now in function")

funaname()

#To find whether no. is even or not by using function calling method
def evoddfun(x):
    print(x,"is passed")
    if(x%2==0):
        print(x,"is even")
    else:
        print(x,"is odd")

evoddfun(3)
evoddfun(4)

#program to find whther no. is divisible by 9 or not 
def check(x):
    print(x,"is passed")
    if(x%9==0):
        print(x,"is divisible by 9")
    else:
        print(x,"is not divisible by 9")
check(81)
check(172)