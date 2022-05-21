# *********************************************
# Magic Methods Mega Brain Eater and Skull Crawler Exercise
# Khali Bank Ltd Exercise 4 Non Public Name Mangling
# ////////////////////////////////////////////////////////////////////

# Double Leading Underscore: __var :Name Mingled to avoind Conflicts

import datetime


class Account():
	
	@staticmethod
	def _current_time(self):
		time = datetime.datetime.now()
		return time
	
	def __init__(self, name, balance):
		self._name = name
		self.__balance = balance
		print(f'Account created for {name}')
		self.trans_list = [(Account._current_time(self), balance)]
		self.show_tans()
	
	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.show()
			self.trans_list.append((Account._current_time(self), amount))
	
	def withdraw(self, amount):
		# 0 < amount <= self.__balance
		if amount > 0 and self.__balance >= amount:
			self.__balance -= amount
			self.show()
			self.trans_list.append((Account._current_time(self), -amount))
		else:
			print(f'Paon Poan {self._name}, You are Bankcurrup')
	
	def show(self):
		print(f'{self._name} __balance is {self.__balance}')
	
	def show_tans(self):
		for date, amount in self.trans_list:
			if amount > 0:
				trans_type = 'Deposit'
			else:
				trans_type = 'Withdraw'
				amount *= -1
			print(f'Amount {amount} dollar,{trans_type} on {date}')

# Mohsin  = Account('Mohsin', 15)
# # Mohsin._balance = 200  # programmer requesting
# Mohsin.__balance = 200  # python enforcing
# # Mohsin._Account__balance = 200
# print(Mohsin.__dict__)
# Mohsin.deposit(5)
# Mohsin.withdraw(10)
# Mohsin.show_tans()


# Double Leading and Trailing Underscore: __var__ : Magic Methods

# print(dir(Account))