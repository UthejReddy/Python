
import re

email = "kjahsdjh@com  ijadfk.com  @slkdjfj.com jdhfihad@.com ldhfuh43@.com"

print("email matches = ",len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))



