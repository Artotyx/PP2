def d(n):
    while n >= 0:
        yield n
        n -= 1
n=int(input('Enter num: '))
for num in d(n):
    print(num)