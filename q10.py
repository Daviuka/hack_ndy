'''10. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
• o número digitado ao quadrado;
• o número digitado ao cubo;
• a raiz quadrada do número digitado;
• a raiz cúbica do número digitado.'''

num = int(input('Digite o número diferente de 0 e positivo: ')) #entrada de dados e tratamento

#operadores matemáticos
quadrado = num**2
cubo = num**3
raiz_quadrada = num**0.5
raiz_cubica = num**0.33333333333333

print(f'O número ao quadrado: {quadrado}, ao cubo igual: {cubo}, sua raiz quadrada é: {raiz_quadrada} e por fim sua raiz cúbica é: {raiz_cubica:.2f}.')


