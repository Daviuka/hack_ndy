'''Faça um programa que receba o salário de um funcionário e o percentual de aumento,
calcule e mostre o valor do aumento e o novo salário.'''

salario= int(input('Digite o seu salário: ')) # Entrada de dados do usuário

#Operadores matemáticos
reajuste= 0.25 * salario  
novo_salario= reajuste + salario

print(f'O seu novo salário será de {novo_salario} e o valor do aumento será de : {reajuste}')