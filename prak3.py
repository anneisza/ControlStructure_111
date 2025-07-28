#Write a PYTHON program to print Fibonacci series up to n!

n = int(input("Masukkan nilai n untuk batas deret Fibonacci: "))

a, b = 0, 1

print("Deret fibonacci hingga", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b