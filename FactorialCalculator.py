num = int(input())
product = 1;

# While Loop Solution
'''
while num > 1:
    product *= num
    num -= 1

print(product)
'''

# For Loop Solution
for num in range(num, 1, -1):
    product *= num

print(product)
