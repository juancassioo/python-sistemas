n = int(input('Digite um número: '))
c = n
f = 1
print('-='*10)
print('Calculando:')
while c > 0:
    print('{}'.format(c), end= ' ')
    print('x' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
print('-='*10)