def s(a, b):
    if a < b:
        for i in range(a, b + 1):
            yield i ** 2
    else:
        print("a should be less than b")

a = int(input("a: "))
b = int(input("b: "))
for j in s(a, b):
    print(j)