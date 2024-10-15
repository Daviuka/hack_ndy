'''15. Escreva um algoritmo que efetue o cálculo de uma prestação em atraso, sendo dados o
valor inicial da prestação, a taxa de juros e o tempo de atraso em dias. Utilize a fórmula
abaixo:'''

vi=int(input('Digite o valor inicial: ')) #entrada de dados
qt_dias_atraso = int(input('Digite o números de dias atrasados: '))
taxa = int(input('Digite o valor da taxa de juros:'))

#fórmula
p_atrasada= vi+(vi*(taxa)/100*qt_dias_atraso)


