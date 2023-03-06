def puissance(n, total):
    if n != 0:
        total = 3 * puissance(n -1, total)
    
    return total

print(puissance(2, 1))