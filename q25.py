import os 
os.system('cls')

#Solicitamso que o usuário que digiteuma letra
letra = input('Digite uma letra').lower()

#verifica se é uma vogal ou cosoante
if letra in ['a','e','i','o','u']:
    print(f'A letra {letra} é uma vogal')
elif letra.isalpha() and len(letra) == 1:
    print(f'A letra {letra} é uma cosoante.')
else:
    print('Entrada inválida. Por favo, digite apenas uma letra')
