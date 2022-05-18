# Methods Mega Brain Eater and Skull Crawler Exercise
# Khali Bank Ltd Exercise 3 Transaction list with Static Method
import datetime
# class Account():
#
#  @staticmethod
#  def _current_time(self):
#     time = datetime.datetime.now()
#     return time
#
#  def __init__(self,_name,__balance):
#     self._name = _name
#     self.__balance = __balance
#     print(f'Account created for {_name}')
#     self.trans_list = [(Account._current_time(self),__balance)]
#     self.show_tans()
#
#  def deposit(self,amount):
#     if amount > 0:
#        self.__balance += amount
#        self.show()
#        self.trans_list.append((Account._current_time(self),amount))
#
#  def withdraw(self,amount):
#     # 0 < amount <= self.__balance
#     if amount > 0 and self.__balance >= amount:
#        self.__balance -= amount
#        self.show()
#        self.trans_list.append((Account._current_time(self), -amount))
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
# Mohsin  = Account('Mohsin', 10)
# Mohsin.deposit(10)
#
# Mohsin.show_tans()
# John  = Account('John', 100)
# John.deposit(10)
# John.withdraw(120)
# John.show_tans()

# *********************************************