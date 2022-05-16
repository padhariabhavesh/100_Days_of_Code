# Generator

#
# import sys
# # Generators
# def my_gen(n:int):
#  start  = 0
#  while start < n:
#     print(f'My_range is returning:{start}')
#     yield start
#     start += 1
# gen_list = my_gen(10)
# print(next(gen_list))
# print(next(gen_list))
# print(next(gen_list))
# print(f'This generator takes {sys.getsizeof(gen_list)} bytes')
#
# print('x'*20)
# itr_list = []
# for val in gen_list:
#  itr_list.append(val)
#
# print(f'This Normal list takes {sys.getsizeof(itr_list)} bytes')
#
#
# print('x'*20)
# itr_list = []
# for val in gen_list:
#  itr_list.append(val)
#
# print(f'This Normal list takes {sys.getsizeof(itr_list)} bytes')
#
# print(itr_list)