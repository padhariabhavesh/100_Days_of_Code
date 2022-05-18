# Class Name Spaces
print('x'*20)
# print(kattle.__dict__)
# print(hamilton.__dict__)
# print(kenwood.__dict__)
# print('x'*20)
# # kenwood.model = 2019
# # print(kattle.__dict__)
# # print(hamilton.__dict__)
# # print(kenwood.__dict__)
# print('x'*20)
kattle.power_src = 'steam'
print(hamilton.power_src)
print(kenwood.power_src)
print(kattle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)
print('x'*20)
hamilton.power_src = 'DC'
kenwood.power_src = 'AC'
print(kattle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)