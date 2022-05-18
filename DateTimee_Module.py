# Date time module in bank project

# Methods Mega Brain Eater and Skull Crawler Exercise
# Khali Bank Ltd Exercise 2 Transaction list

import datetime
#
#
# class Account():
#
#  def __init__(self,_name,__balance):
#     self._name = _name
#     self.__balance = __balance
#     print(f'Account created for {_name}')
#     self.trans_list = []
#
#  def deposit(self,amount):
#     if amount > 0:
#        self.__balance += amount
#        self.show()
#        self.trans_list.append((datetime.datetime.now(),amount))
#
#  def withdraw(self,amount):
#     # 0 < amount <= self.__balance
#     if amount > 0 and self.__balance >= amount:
#        self.__balance -= amount
#        self.show()
#     else:
#        print(f'Paon Poan {self._name}, You are Bankcurrup')
#
#  def show(self):
#     print(f'{self._name} __balance is {self.__balance}')
#
#  def show_tans(self):
#     for date,amount in self.trans_list:
#        if amount > 0 :
#           trans_type = 'Deposit'
#        else:
#           trans_type = 'Withdraw'
#           amount *= -1
#        print(f'Amount {amount} dollar,{trans_type} on {date}')
#
#
#
# Mohsin  = Account('Mohsin', 10)
# Mohsin.deposit(10)
# Mohsin.show_tans()
# John  = Account('John', 100)
# John.deposit(10)
# John.withdraw(120)
# John.show_tans()
# *********************************************