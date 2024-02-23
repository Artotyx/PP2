def a(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Take input from the user
n = int(input("Enter a number: "))
print("divisible by 3 and 4 between 0 and", n, ":", end=" ")
for num in a(n):
    print(num, end=" ")