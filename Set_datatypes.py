# Sets data types

A = {'A', 'B', 'B', 'D', 'A'}
B = {'X', 'V', 'C', 'X', 'B'}

print(A)
print(B)
C = A.intersection(B)
D = A.union(B)
print(C)
print(D)

A.add('John cena')
A.update(['John2'])
A.remove('John2')
A.remove('John cena')
del A
print(len(A))