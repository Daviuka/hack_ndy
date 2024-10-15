def verificar_multiplo_3(numero):
    if numero % 3 == 0:
        print(f'O numero {numero} é multiplo de 3.')
    else:
        print(f'O número {numero} não é multiplo de 3.')

#Digite um número
numero = int(input('Digite um numero inteiro: '))
verificar_multiplo_3(numero)            