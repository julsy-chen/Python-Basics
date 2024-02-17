# Factoring Program

num = int(input("Enter a number: "))
stop = int(num ** 0.5) + 1

for temp in range(1, stop): 
    if num % temp == 0:
        print(temp)
        print(num/temp)



