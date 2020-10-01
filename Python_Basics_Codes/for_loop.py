

##EXAMPLE 01
for variable in range(0,10):
    print(variable)
    
    
 
##EXAMPLE 02
list_example=[0,1,2,5,8,7]
for index in range(0,len(list_example)):
    list_example[index]=list_example[index] + 2
print(list_example)



list_2= ["apple","banana","cake","Drink","animal"]
for item in list_2:
    if(item == "cake"):
        print("HELLO")
    else:
        print(item)
        

for i in range(0,10):
    summation = summation + i
print(summation)


##Even OR Odd program
int_list = [10,20,54,8,45,11,16,13]
for integer in int_list:
    if(integer%2==0):
        print("even")
    else:
        print("odd")