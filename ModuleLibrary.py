# Random generator
# Age Day
import datetime
import random
# x = random.randint(1,10)
# print(x)
# date  = datetime.datetime.now()
# print(date)
# DOB = datetime.date(1994,5,27)
# today = datetime.date.today()
# Age = today - DOB
# print(Age)
from comp import list_s

print(list_s)
import random
import datetime
import timeit

print('-'.join(str(n) for n in range(10000)))
print(timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000))

# x = random.randint(1,10)
# print(x)
#
# date = datetime.datetime.now()
# print(date)
#
#
# dob = datetime.date(1991,3,11)
#
# today = datetime.date.today()
# age = today-dob
# print(age)