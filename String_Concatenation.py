# String Concatenation - Add two strings
name = "Gangster"
job = " Play cricket"
print(name + job)

# String multiplication
print(name * 10)

# Data type strings
a = '1'
b = '2'
print(a + b)

# Strings concatenation in variables
string1 = 'This'
string2 = 'Ok'
print(string1 + ' is demo ' + string2)

# String formatting
name = 'Bhavesh'
age = 27
# f define placeholder to variables
Message = f'Hello {name} you are {age} years old'  # New method
Message1 = 'Hello {0} you are {1} years old'.format(name, age)  # Old method
print(Message)
print(Message1)

# String formatting advance method
Name = input('Plese enter your name:')
Age = input('Plese enter your age:')
Message2 = f'Hello {Name} you are {Age} years old'
print(Message2)

# Dynamic value
Name = input('Plese enter your name:')
Age1 = 27
Message3 = f'Hello {Name} you are {Age1 / 2} years old'
print(Message3)

# Built in function (int)
Name = input('Plese enter your name:')
Age1 = int(input('Plese enter your age:'))
Message4 = f'Hello {Name} you are {Age1 - 6} years old'
print(Message4)

# Back slash escape character (\'s, \ts TAB, \ns NEW LINE)
Name = input('Plese enter your name:')
Age2 = int(input('Plese enter your age:'))
Message5 = f'Hello {Name} welcome , your\'s age is  {Age2 - 6} years old'
print(Message5)
