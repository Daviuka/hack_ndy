def potencia(base, expoente):
    return base ** expoente

#Exenplo do uso
base = float(input('Digite o primeiro numero (maior que zero):'))
expoente = float(input('Digite o segundo numero (maior que zero):'))

if base > 0 and expoente > 0:
    resultado = potencia(base, expoente)
    print(f"{base} elevado a {expoente} é: {resultado}")
else:
    print('Ambos os números precisam ser maiores que zero.')    


