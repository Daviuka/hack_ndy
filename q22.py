import os
os.system('cls')

# Para começar, solicitamos que o usuário digite um número inteiro
# entre 1 e 7

numero = int(input("Digite um número entre 1 e 7: "))


#Verificamos o número e exibimos o dia da semana correspondente

if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-Feira')
elif numero == 3:
    print('Terça-Feira')
elif numero == 4:
    print('Quarta-Feira')
elif numero == 5:
    print("Quinta-Feira")
elif numero == 6:
    print("Sexta-Feira")
elif numero == 7:
    print('Sábado')
else:
    print('Não existe dia da semana correspondente a esse número.')
    