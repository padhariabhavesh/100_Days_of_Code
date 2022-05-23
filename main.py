# Follow the code file
'''
 main.py
 playerclass.py
 enemyclass.py
'''

#
# from player import Player
# #
# #
# # Mohsin   = Player('Mohsin')
# # # print(Mohsin.name)
# # # print(Mohsin.lives)
# #
# # Mohsin.lives -= 1
# # print(Mohsin)
# #
# # Mohsin.lives -= 1
# # print(Mohsin)
# #
# # Mohsin.level = 2
# # print(Mohsin)
# # Mohsin.level += 5
# # print(Mohsin)


from enemy import Enemy, Bone_snacher, Blood_drinker, KingBloodDrinker

# big_teeth = Enemy('Big Teeth',12,1)
#
# print(big_teeth)
# big_teeth.take_damage(4)
# print(big_teeth)
# big_teeth.take_damage(8)
# print(big_teeth)
# big_teeth.take_damage(8)
# print(big_teeth)

# Method Overloading, Changin Method in Subclass
# ugly_snacher = Bone_snacher('Blood Drinker')
# print(ugly_snacher)
# print(ugly_snacher.snatch())
# # Super Method Change

# ugly_snacher = Bone_snacher('Blood Drinker')
# Vampire = Blood_drinker('Blood Drinker')
# while Vampire.lives:
#  # if not Vampire.Ducked():
#  Vampire.take_damage(1)
#  # print(Vampire)


BloodBath = KingBloodDrinker('BloodBath')
print(BloodBath)
BloodBath.take_damage(12)
print(BloodBath)