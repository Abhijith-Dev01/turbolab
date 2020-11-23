import datetime
def server_cost(x1,x2):
    if (x2==x1):
        return 20
    elif (x2.day!=x1.day) and (x2.month==x1.month):
        d1=int(x1.day)
        d2=int(x2.day)
        diff=d2-d1
        return 30*diff
    elif (x2.month!=x1.month) and (x2.year==x1.year):
        m1 = int(x1.month)
        m2 = int(x2.month)
        diff = m2 - m1
        return 1000*diff
    else:
        return 20000
d1=int(input("enter the day created "))
m1=int(input("enter the month created "))
y1=int(input("enter the year created "))
d2=int(input("enter the day deleted "))
m2=int(input("enter the month deleted "))
y2=int(input("enter the year deleted "))
x1=datetime.datetime(y1,m1,d1)
x2=datetime.datetime(y2,m2,d2)
c=server_cost(x1,x2)
print("the server cost is:",c)
# OUTPUT
# enter the day created 6
# enter the month created 6
# enter the year created 2020
# enter the day deleted 9
# enter the month deleted 6
# enter the year deleted 2020
# the server cost is: 90
