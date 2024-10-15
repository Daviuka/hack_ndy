'''6. Faça um programa que receba o salário base de um funcionário, calcule e mostre seu
salário a receber, sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto
de 10% sobre o salário base.'''

salario= int(input('Digite o seu salário: ')) # Entrada de dados do usuário

#Operadores matemáticos
imposto= 0.1 * salario  
bonificacao= salario + 50
salario_final= bonificacao - imposto

print(f'O seu salario com impostos e reajuste será de: {salario_final}:')