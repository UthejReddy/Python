## Whileloop Statement

a=1
s=0
x=0
print("enter number to add to the sum")
print("enter 0 to Quit")
while a!=0:
    print("current sum:",s)
    a=float(input("enter number :"))
    s=s+a
print("total sum is:",s)