import os
import datetime

def func1(y,m,d,ms,se,da,mi):

    input_date = datetime.date(y,m,d)
    input_date1= datetime.datetime(y,m,d) + datetime.timedelta(microseconds=ms,seconds=se,minutes=mi,days=da)
    t= input_date1 - datetime.timedelta(microseconds=1,seconds=2,minutes=2,days=3)
   # print (t)
    day = t.strftime("%d")
 #   print (day)
    year= t.strftime("%Y")
 #   print (year)
    month = t.strftime("%B")
 #   print(month)
    minute= t.strftime("%M")
 #   print(minute)
    second= t.strftime("%S")
 #   print(second)
    return input_date,input_date1,t,day,year,month,minute,second

def func2(y,m,d,ms,se,da,mi):
    a = datetime.datetime(year=2020,month=1,day=3,hour=10,minute=34,second=24)
    s = a.strftime("%c")
    x= datetime.datetime(year=y,month=m,microsecond=ms,minute=mi,second=se,day=da)
    q= str(x.strftime("%c"))
    z= datetime.datetime.strptime(q,"%c")
    return x,q,z

if __name__ == "__main__":
    y,m,d,ms,se,da,mi = map(int, input().split())
    inputs=func1(y,m,d,ms,se,da,mi)
    inputs5=func2(y,m,d,ms,se,da,mi)
    print(inputs[0])
    print(inputs[1])
    print(inputs[2])
    print(inputs[3])
    print(inputs[4])
    print(inputs[5])
    print(inputs[6])
    print(inputs[7])
    print(inputs5[0])
    print(inputs5[1])
    print(inputs5[2])



