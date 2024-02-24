#ex1 
def squares_generator(N):
    for i in range(1, N + 1):
        yield i**2

N = int(input())
squares = squares_generator(N)

for square in squares:
    print(square)

#ex2
def evens_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
evens = evens_generator(n)
for even in evens:
    print(even)

#ex3
def divisible_generator(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i
n = int(input())
divisible = divisible_generator(n)
for divides in divisible:
    print(divides)

#ex4
def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i**2
a = int(input())
b = int(input())
square = squares_generator(a, b)
for squares in square:
    print(squares)

#ex5
def down_zero_generator(n):
    for i in range(n, n - n - 1, -1):
        yield i
n = int(input())
to_zero = down_zero_generator(n)
for zeros in to_zero:
    print(zeros)