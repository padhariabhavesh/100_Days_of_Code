list_ = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

list_s = []

for letter in list_:
	if 'G' not in letter:
		list_s.append(letter)
	else:
		list_s.append('Letter was skipped')

print(list_s)
print('X' * 20)

list_sc = [letter for letter in list_ if 'G' not in letter]
print(list_sc)

print('X' * 20)

list_scx = [letter if 'G' not in letter else 'Letter was skipped' for letter in list_]
print(list_scx)