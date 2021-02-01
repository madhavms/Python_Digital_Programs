def find_nth_term(n):
    if n % 2 == 0:
        pow = (n - 2) / 2
        return int(3 ** pow)
    else:
        pow = (n - 1) / 2
        return int(2 ** pow)


n = int(input("Enter which term to find:"))
print("The {} term is {}".format(n,find_nth_term(n)))
