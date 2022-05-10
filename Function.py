# Function defination
# y = x +2
#
#
# def Turnonlight(input):
#  statement or Block of code
# #    return something
#
# def add2(x):
#  y = x +2
#  print(y)
#
#
# add2(2)
#

# what is *args

# def greet(*args):
#  print(args)
#  # a,b,c,d = args
#  print('Hello '+args[0]+' How are you')
#  print('Hello ' +args[1] + ' I dont know you')
#  print('Hello ' + args[2] + ' I dont know you')
#
# greet('Samy','Mohsin','John', 'Bally')
#
# def sum_fun(*args):
#  print(args)
#  result = 0
#  for x in args:
#     result += x
#  return print(result)
#
# sum_fun(1,2,3,4,5)

# *args summary

# def greet(name,*args,named_value,**kwargs):
#  print(f'Hello {name}')
#  print(args)
#  for i in args:
#     print(f'Hello {i}')
#  print(f'Hello {named_value}')
#
# greet('Mohsin','Mohsin1','Mohsin2','Mohsin3',named_value= 'Mohsinnamed')
# what is **kwargs


# def myfun(**kwargs):
#
#  for key , value in kwargs.items():
#     print(f'key:{key} and value is {value}')
#
#
# a = {"fname":'Mohsin',"mname":'John',"lname":'kally',"fname1":'Mohsin',"mname1":'John',"lname1":'kally'}
# myfun(**a)

# Scope of Function