#Write a PYTHON program to produce following design

    #1

    #2 2

    #3 3 3

    #4 4 4 4 

    #5 5 5 5 5

    #If user enters n value as 5

n = int(input("Masukkan nilai n: "))

print("Desain pola:")
for i in range(1, n + 1):
    print((str(i) + " ") * i)