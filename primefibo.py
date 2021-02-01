"""
Problem
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ……..
This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order.

Write a program to print the first N terms of the fibo-prime series
"""

def checkprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fib = [1,1]
    for i in range(1,n):
        fib.append(fib[i-1]+fib[i])
    return fib

def generate_prime(n):

    prime = []
    for i in range(2,1000):
        if len(prime) >= n:
            return prime
        if checkprime(i):
            prime.append(i)


def fiboprime(n):
    fib = fibo(n)
    prime = generate_prime(n)

    prime_fibo = []
    for i in range(0,n):
        if len(prime_fibo) == n:
            return prime_fibo
        prime_fibo.append(fib[i])
        prime_fibo.append(prime[i])


    return prime_fibo

print("Prime-Fibo series = {}".format(fiboprime(14)))