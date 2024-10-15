def calcular_salario(horas_trabalhadas, salario_minimo):
    #A hora trabalhada vale a metade do salario_minimo
    valor_hora = salario_minimo / 2
    #Salario bruto
    salario_bruto = horas_trabalhadas * valor_hora  
    # Imposto de 3% sobre o salrio bruto
    imposto = salario_bruto * 0.03  
    # Salario_liquido a receber
    salario_liquido = salario_bruto - imposto
    return salario_bruto, imposto, salario_liquido

#Digite os numeros
horas_trabalhadas = float(input('Digite o número de horas trabalhadas: '))
salario_minimo = float(input('Digite o valor do salario_minimo: ')) 

salario_bruto, imposto, salario_liquido = calcular_salario(horas_trabalhadas, salario_minimo)

print(f'Salario bruto: R${salario_bruto:.2f}')
print(f'Imposto (3%): R${imposto:.2f}')
print(f'Salario a receber: R${salario_liquido:.2f}')