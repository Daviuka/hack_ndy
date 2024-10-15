def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f'O numero {numero} é PAR.')
    else:
        print(f'O numero {numero} é IMPAR.') 

#Digite um numero
numero = int(input('Digite um número inteiro: '))
verificar_par_impar(numero)

