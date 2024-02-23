def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter num: "))
even_nums = even(n)
print("Even numbers between 0 and", n, ":", end=" ")
print(*even_nums, sep=", ")