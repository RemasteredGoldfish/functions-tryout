print ('fibonacci something')
a = int(input('hoeveel getallen in een rij wil je krijgen?'))

def fibonacci(n):
    a, b = 0, 1
    for getal in range(n):
        yield a                 
        a, b = b, a + b
print(list(fibonacci(a)))