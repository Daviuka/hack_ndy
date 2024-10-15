import os
os.system('cls')

# Para começar, definimos quais variáveis são
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite outro número: '))

#Calculamos a divisão com os números que o usuário informará
div = a/b

if a / b:
    print(f'Letra a que é {a} é divisível por b que é {b}')
else:
    print('A letra a não é divisível por b')