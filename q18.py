#Para começar, solicitamos que o usuário coloca as informações 

percuso = float(input('Digite o percuso da viagem em km: '))
tipo_carro = input('Digite o tipo do carro (A, B ou C): ').upper
preco_combustivel = float(input('Digite o preço do litro do combustivel em reais: '))

# Definimos o consumo de combustivel para cada tipo de carro
if tipo_carro == 'A':
    consumo_por_hora = 16
elif tipo_carro == 'B':
    consumo_por_hora = 12
elif tipo_carro == 'C':
    consumo_por_hora = 8
else:
    print('Tipo de carro inválido. Escolha entre A, B e C.')
    consumo_por_km = None

#Agora, calculamos o consumo e o custo se o tipo de carro for valido
if consumo_por_km:
    litro_necessario = percuso / consumo_por_hora
    custo_estimado = litro_necessario * preco_combustivel

#Para finalizar, exibimos os resultados
print(f'O consumo estimado de combustivel é:{litro_necessario} litros')
print(f'O custo estimado da viagem é: R${custo_estimado}')