'''16. Faça um programa que receba o peso de uma pessoa, calcule e mostre:
• o novo peso, caso a pessoa engorde 15% sobre o seu peso original;

• o novo peso, caso a pessoa emagreça 20% sobre o seu peso original.'''

peso=int(input('Digite o seu peso: ')) #entrada de dados

#operações indicadas
engordou = (peso*0.15 ) + peso
emagreceu = (peso*0.2) - peso

print(f'Se a pessoa engorda 15% do peso: {engordou}, se a pessoa emagrece 20% do peso{emagreceu}.')