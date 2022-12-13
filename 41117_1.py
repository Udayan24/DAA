# 41117 - Udayan Chavan (P1)
# -------------------------------------------
# Fibonacci series:
# 0 1 2 3 4 5 6 7  8  9  10 11
# 0 1 1 2 3 5 8 13 21 34 56 90
# -------------------------------------------
# -- Fibonacci numbers using recursion --
def fibonacciR(n):
    if n<=1:
        return n;
    return fibonacciR(n-1) + fibonacciR(n-2)

# -------------------------------------------
# -- Fibonacci numbers without using recursion --
def fibonacci(n):
    f0 = 0
    f1 = 1
    if n<0:
        print("Invalid Input") 
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f1

# -------------------------------------------
x = int(input("Enter 0: Recursive method and 1: Non-Recursive method: "))
n = int(input("Enter n for n^th fibonacci number: "))

if x==0:
    print(fibonacciR(n))
elif x==1:
    print(fibonacci(n))
else:
    print("Invalid input")