import os
os.system('cls')

# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Remove espaços em branco e calcula o comprimento da palavra
quantidade_letras = len(palavra.replace(" ", ""))

# Verifica se a quantidade de letras é par ou ímpar
if quantidade_letras % 2 == 0:
    print(f"A quantidade de letras na palavra '{palavra}' é par.")
else:
    print(f"A quantidade de letras na palavra '{palavra}' é ímpar.")
