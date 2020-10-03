import datetime
from datetime import time
from datetime import datetime
#example 1
date_object1 = datetime.datetime.now()
print(date_object1)


#example 2
date_object2 = datetime.date.today()
print(date_object2)

#example 3
date_object3 = datetime.date(2019,4,10)
print(date_object3)

#example 4
timestamp=datetime.date.fromtimestamp(5465645414)
print("date=" ,timestamp)


#example 5
today=datetime.date.today()
print("current year:",today.year)
print("current month:",today.month)
print("current day:",today.day)

#example 6

a = time()
print("a=",a)

b = time(10,22,45)
print("b=",b)

#Example 7
t1=datetime.date(year=2020,month=6,day=7)
t2=datetime.date(year=2017,month=4,day=16)
t3=t1-t2
print("t3=",t3)




#Exapmle 8
now = datetime.now()
datetime.strftime(now,'%y')