#create an object
elements=input("enter numbers :")
list=elements.split(",")
tuple=(*list,)
print("list:",list)
print("tuple:",tuple)


#create a list
color_list=["red","green","white","black"]
print(color_list[0],color_list[3])


#import datetime library
import datetime
date1=2014,7,11
date2=2014,7,2


list1=[1,4,6,8,4,9,4]
number=4
count=list1.count(number)
count


#create dictionary
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
result={dic1+dic2+dic3}
result


#import library pandas
import pandas as pd
ser1=pd.Series([2,4,6,8,10])
ser2=pd.Series([1,3,5,7,9])
add=ser1 + ser2
add

sub=ser1+ser2
sub

mullti=ser1*ser2
mullti
