import random

n = random.randint(14, 18)
b = random.randint(8, 14)
a = random.randint(3, 7)
print(f'n = {n}   a = {a},  b = {b}')
nums = [x for x in range(n)]
print(nums)
nums[a:b+1] = []
print(nums)

str = '12.34 56.78'
flag = False
num1, num2 = '', ''
for chr in str:
    num