start = int(input())
end = int(input())

# for loop
for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else: print(start) 

# while loop
while start <=end:
    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else: print(start)
    start += 1