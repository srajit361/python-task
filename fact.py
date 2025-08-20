def factorial(n):
    if (n<2):
        return 1
    else:
        return n*(factorial(n-1))
z=factorial(int(input("enter the number:")))
print(z)