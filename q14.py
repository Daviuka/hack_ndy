'''14. Escreva um algoritmo que leia a base e a altura de um retângulo e calcule a sua área, o
seu perímetro e a sua diagonal, sabendo que:'''

base = int(input('Digite o valor da base:')) #entrada de dado do usuário
altura = int(input('Digite o valor da base:'))

#operadores matemáticos
area= base*altura
perimetro=(base*2)+(altura*2)
diagonal=((base**2)+(altura**2))**0.5


print(f'O cálculo da área será igual a: {area}, o perímetro será de: {perimetro} e a quantidade de diagonais é: {diagonal}')