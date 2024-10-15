'''4. Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que este sofreu um aumento de 25%.'''

salario= int(input('Digite o seu salário: ')) # O usuário digita o valor

#Operadores matemáticos
reajuste= 0.25 * salario  
novo_salario= reajuste + salario

print(f'O seu novo salário será de {novo_salario}')