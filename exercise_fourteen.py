# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

k = 1
n = 5
while n >= k:
    for i in range(n):
        print('*', end=' ')
    print()
    n = n - 1
