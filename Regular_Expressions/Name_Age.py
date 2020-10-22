#regular expression code to sort the statement

#import library
import re

nameage = "Janice is 22 and Tom is 34 Amit is 23 Sham is 32 Shubham is 25"

ages = re.findall(r'\d{1,3}',nameage)
names = re.findall(r'[A-Z][a-z]*',nameage)

print(ages)
print(names)


