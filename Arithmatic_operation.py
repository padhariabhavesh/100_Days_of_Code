# Arithmatic operation
'''
+ Addition
- Subtraction
* Multiplication
** Exponent
/ Division
// Double division
() Parenthesis
% Module
Sequence of operation
	- Parenthesis
	- Exponent
	- Division
	- Multiplication
	- Addition
	- Subtraction
- PEDMAS

'''

a = 10
b = 25

print(a+b,'Addition')
print(a-b,'Subtraction')
print(a*b,'Multiplication')
print(a/b,'Division')
print(a//b,'Whole Number')
print(a%b,'Module')
print(a**b, 'Exponent')
print(a+(a*b)+b-a, 'Parenthesis')
print(2-2*2,'PADMAS')
print((3-2)*3**2*a%b*a//b/a%b,'PADMAS')