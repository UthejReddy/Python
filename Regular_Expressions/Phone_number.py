import re

phone="457-154-6566"

if re.search("\d{3}-\d{3}-\d{4}",phone):
    print("its a valid number")
else:
    print("its not a valid nnumber")