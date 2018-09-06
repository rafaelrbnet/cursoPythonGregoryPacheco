def calcula_dobro(numero):
    total = numero * 2
    return total


def calcula_soma_numeros(n1, n2, n3):
    total = n1 + n2 + n3
    return total


def calcula_n_numeros(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


resultado = calcula_dobro(8)
print('O resultado do dobro de 8 é {} '.format(calcula_dobro(8)))
print('O resultado da soma de 3 números é {}'.format(calcula_soma_numeros(1, 2, 3)))
print('O resultado da soma de vários números é {}'.format(calcula_n_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
