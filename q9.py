'''9. Escreva um algoritmo que leia os valores dos catetos de um triângulo retângulo e mostre
qual é o valor da hipotenusa desse triângulo.'''

b = int(input('Digite a medida do cateto 1 : ')) #entrada de dados e tratamento
c = int(input('Digite a medida do cateto 2: '))

#teorema de pitágoras
hipotenusa = b**2 + c**2
a=hipotenusa**0.5

print(f'Hipotenusa é igual a : {a}')




