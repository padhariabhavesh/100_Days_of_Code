# if statement

# x = int(input('Please enter a value to check:'))
#
# if x>2:
#  print('I run because if is true')
# else:
#  print('I am running because if is false')

# marks = int(input('Please enter your marks:'))
# passing_marks = 50
#
# if marks > passing_marks:
#  print('Congratulations you passed')
# else:
#  print('Poan poan you failed')

# sound = input('What sound you like:')
#
# if sound == 'meo':
#  print('You love cats, cat person')
# elif sound == 'wuf':
#  print('You love dogs, you dog person')
# elif sound == 'wuf':
#  print('You love dogs, you dog person')
# elif sound == 'wuf':
#  print('You love dogs, you dog person')
# elif sound == 'wuf':
#  print('You love dogs, you dog person')
# elif sound == 'wuf':
#  print('You love dogs, you dog person')
# else:
#  print('You dont love cats')


# name = input('Please enter your name:')
#
# if name == 'Mohsin':
#  print(f'Hello {name}, Please enter ')
# elif name == 'john':
#  print(f'Hello {name}, Please enter ')
# elif name == 'sally':
#  print(f'Hello {name}, Please enter ')
# else:
#  print('I dont know you')


# amount = int(input('Please enter your amount:'))
#
# if amount < 1000:
#  discount = amount*0.05
#  print(f'Discount is {discount} ')
# elif amount < 5000:
#  discount = amount*0.1
#  print(f'Discount is {discount} ')
# else:
#  discount = amount*0.15
#  print(f'Discount is {discount} ')

# # Jungle rescuer
# x = input('Please enter first location:')
# y = input('Please enter second location:')
#
# if x == 'Right':
#  if y == 'Up':
#     print(f'you are in {x} and {y} direction')
#  else:
#     print(f'you are in {x} and {y} direction')
# else:
#  if y == 'Up':
#     print(f'you are in {x} and {y} direction')
#  else:
#     print(f'you are in {x} and {y} direction')
# #


# num  = int(input('Please enter your num: '))
#
# if num>5 or num<10:
#  print('You number is in limits')


# sentance = 'A quick brwon fox jumps over the lazy Dog'
#
# word = input('Please enter the word to check: ')
#
# if word in sentance:
#  print('This word exit in senctance')
# else:
#  print(f'{word} does not exist in sentance')
#
# Article Analyzer
# article = """  Python is a higher level programming language than most other languages. It is object oriented , but not as
# ironically as Java can be ; suitable,
# among other uses, to develop distributed applications , scripting , numerical computation and system testing .
#  It is often also studied among the first languages ​​for its similarity to a pseudo-code. It is also often used to
#   simulate the creation of those programs that perhaps should be implemented in other languages, but testing them
#    in Python allows the programmer to rearrange ideas about it (such as creating a game via Pygame or a social network via Flask ). """
#
#
#
# word = input('Please enter the word to check: ')
#
# if word in article:
#  print(f'This article is about {word}')
# else:
#  print('I dont know what this article is about')

# Some Unusual Conditions

# if 1:
#  print('There is true with if')
#
# else:
#  print('Zero is considered false')

# x,y = 5,7
#
# if x+y:
#  print('Yes expresion return true')
# else:
#  print('I print when its False')
#
# list_a = []
# if list_a:
#  print('I run becasue if is with true')
# else:
#  print("Empty container is false")


# For and if together Exercise


# Exercise


# ip = "23112,32154,564,897,564,13,3164,546,31"
# print(ip)
#
# cln_num= ''
# for i in range(0,len(ip)):
#  if ip[i] in '0123456789':
#     cln_num = cln_num + ip[i]
# cln_int = int(cln_num)
# print(cln_int)

# Exercise continue and break

# for i in range(10):
#  # inside for loop
#
#  if condition:
#
#     continue
#     # inside if condition
#
#  # inside for loop
#
# # Code outside for loop
#
# # ## ## ## ## ## ## ## ## ## ## ## ## #
#
# for i in range(10):
#
#  # inside for loop
#  if condition:
#
#     break
#     #code inside if condition
#
#  # inside for loop
#
# # Code outside for loop


# for val in 'string':
#
#  if val == 'i':
#     break
#  print(val)
# print('end loop')
#
# grecy_list = ['milk','pasta','eggs','cheez','bread','rice']
#
# for i in grecy_list:
#
#  if i == 'cheez':
#     print('I dont buy '+ i)
#     continue
#     print('I dont buy ' + i)
#  print('I buy '+i)

# Advance Exercise
# Program to check if a number is prime or not

# num = int(input('Please enter number: '))
#
# if num > 1:
#  for i in range(2,num):
#     if num % i== 0:
#        print(f'{num} is not Prime Number')
#        print(f'{i} times,{num//i} is {num}')
#        break
#
#  else:
#     print(f'{num} is Prime Number woooaaaa')
# else:
#  print(f'{num} is not prime Number')

# Exercise Challane
# Word Counter

# article = """Python is a higher level programming language than most other languages. It is object oriented , but not as
# ironically as Java can be ; suitable,
# among other uses, to develop distributed applications , scripting , numerical computation and system testing .
# It is often also studied among the first languages ​​for its similarity to a pseudo-code. It is also often used to
# simulate the creation of those programs that perhaps should be implemented in other languages, but testing them
# in Python allows the programmer to rearrange ideas about it (such as creating a game via Pygame or a social network via Flask ). """
#
article = 'A quick brwon fox jumps over the lazy dog'

num = 1
for char in article:
 if char == ' ':
    num += 1
print(f'Number of word in Article are {num}')
