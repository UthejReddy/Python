
#Filter
my_list = [1,5,4,8,12,16]
new = list(filter(lambda x:(x%2==0),my_list))
print(new)



#Mapping
my_list = [1,5,4,8,12,16]
new = list(map(lambda x:x*2,my_list))
print(new)