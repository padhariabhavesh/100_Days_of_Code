# While Loops
# While Loop

# for i in range(10):
#  print(f'{i} times')

# if True:
#  print('Only Once')

# x =1
# while x<10:
#  print(f'{x} is now less than 10')
#  x +=1
# else:
#  print(f'{x} is greater or equal than 10')

# Exercise
# name = 'coding4startups'
#
# i = 0
# while i < len(name):
#  if name[i] =='4':
#     i += 1
#     continue
#  print('Current Letter : '+ name[i])
#  i += 1

# Jungle Rescuer

available_exit = ['UpRight']
chosen_exit = ''

while chosen_exit not in available_exit:
	chosen_exit = input('Tu ye to bta hai kidher: ')
	if chosen_exit == 'UpRight':
		print('You Are saved from Lion King')
		print('Game Won')
		break
else:
	print('You got out on first try')