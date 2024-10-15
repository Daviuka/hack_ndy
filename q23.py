import os
os.system('cls')

#Para começar, definimos as variáveis para o usuário colocar os valores
peso = input('Dighite o seui peso: ')
altura = input('Digite a sua altura: ')

#Calculo o índice de Massa Corporal (IMC)
IMC = peso / altura**2

#Para finalizar, determinamos o grau de obesidade com base no IMC
IMC
print(f'O seu IMC é: {IMC:.2f}')

if IMC < 18.5:
    print('Você está abaixo do Peso!!!')
elif 18.5 <= IMC < 24.9:
    print('Você está Saudável!!')
elif 25 <= IMC < 29.9:
    print('Você está com Sobrepeso!')
elif 30 <= IMC < 34.9:
    print('Você está com Obesidade de Grau I!')
elif 35 <= IMC < 39.9:
    print('Você está com Obesidade de Grau II')
else:
    print('Você está com Obesidade de Grau III!!!')

'''

Magreza = IMC <= 18.5
Saudável = IMC == 18.5, 24.9
Sobrepeso = IMC == 25.0, 29.9
Obesidade de Grau I = IMC == 30.0, 34.9
Obesidade de Grau II = IMC == 35.0, 39.9
Obesidade de Grau III = IMC >= 40.0

'''
