somapar = 0
terceira = 0
maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição {l},{c}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print(f'A soma dos pares foi {somapar}')
for l in range(0,3):
    terceira += matriz[l][2]
print(f'A soma da terceira coluna é {terceira}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'o maior valor da terceira linha foi {maior}')