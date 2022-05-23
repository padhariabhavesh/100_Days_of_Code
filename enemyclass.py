# Follow the code file
'''
 main.py
 playerclass.py
 enemyclass.py
'''
import random


class Enemy:
	
	def __init__(self, name='Enemy', hit_point=0, lives=1):
		self.name = name
		self.hit_points = hit_point
		self.lives = True
	
	def take_damage(self, damage):
		remaining_point = self.hit_points - damage
		if remaining_point >= 0:
			self.hit_points = remaining_point
			print(f'I take bullet took {damage} point damage, my remaing life is {remaining_point}')
		else:
			self.lives -= 1
			if self.lives > 0:
				print(f'{self.name} lost life')
			else:
				print(f'Arrrrgggghhh, {self.name} died')
				self.lives = False
	
	def __str__(self):
		return f'Enemy Name:{self.name}, Enemy lives: {self.lives}, Hit Points:{self.hit_points}'


class Bone_snacher(Enemy):
	
	def __init__(self, name):
		super().__init__(name=name, lives=1, hit_point=23)
	
	def snatch(self):
		return f'I am {self.name}, i just snached you Bone'


class Blood_drinker(Enemy):
	
	def __init__(self, name):
		super().__init__(name=name, lives=3, hit_point=50)
	
	def Ducked(self):
		if random.randint(1, 5) == 5:
			print(f'*****{self.name}:Ducked,and Saved')
			return True
		else:
			return False
	
	def take_damage(self, damage):
		if not self.Ducked():
			super().take_damage(damage=damage)


class KingBloodDrinker(Blood_drinker):
	
	def __init__(self, name):
		super().__init__(name)
		self.hit_points = 150
	
	def take_damage(self, damage):
		super().take_damage(damage // 4)

