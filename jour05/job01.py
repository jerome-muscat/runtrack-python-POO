def factorielle(n, total):
    if n != 0:
        total= n * factorielle(n-1, total)
    return total
total = 1
print(factorielle(5, total))