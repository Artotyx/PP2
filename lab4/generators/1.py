def s(N):
    for i in range(N):
        yield i ** 2

N = int(input("Enter num: "))
for j in s(N):
    print(j)