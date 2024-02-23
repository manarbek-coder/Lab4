def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = 5
b = 6

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)
