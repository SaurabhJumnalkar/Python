#return value from function
def sum(x,y):
    return x+y
print(sum(4,3))

#return variable directly
def time(seco):
    hour=seco//3600
    minu=seco//60
    sec=seco
    return hour,minu,sec

hour,minu,sec=time(3600)
print(hour,minu,sec)