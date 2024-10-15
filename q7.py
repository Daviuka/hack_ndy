'''7. Escreva um programa para ler uma temperatura dada na escala Fahrenheit e exibir o
equivalente em Celsius.'''

temf= int(input('Digite a temperatura: ')) # O usuário digita o valor

tempc= 0.5555555*(temf-32) #conversão de temperatura

print(f'Temperatura convertida é igual: {tempc}')