import os 
os.system('cls')

# Exibe as opções de operação para o usuário
print("Escolha a operação desejada:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Potenciação (^)")

# Lê a escolha do usuário
operacao = input("Digite o número correspondente à operação (1/2/3/4/5): ")

# Solicita os dois números para a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação de acordo com a escolha do usuário
if operacao == '1':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
elif operacao == '5':
    resultado = num1 ** num2
    print(f"Resultado: {num1} ^ {num2} = {resultado}")
else:
    print("Operação inválida. Escolha um número entre 1 e 5.")