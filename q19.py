# Para começar, definimos as variáveis para que o usuário digite
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

#Para saber a diferença entre os 3 número, o min() e o max(), são funções que retornam, respectivamente
# o menor e o maior valor entre os argumentos passados
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)

#Para finalizar, mostramos o resultados de qual é o maior ou menor número que foi digitado
print(f'O número maior é: {maior}')
print(f'O número menor é: {menor}')   
