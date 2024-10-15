def converter_medidas(pes):   
    # 1 pé = 12 polegados
    polegados = pes * 12     
     # 1 jarda = 3 pes
    jardas = pes / 3         
     # 1 milha = 1760 jardas 
    milhas = jardas / 1760
    return polegados, jardas, milhas

#Escreva as medidas
pes = float(input("Digite a medida em pés: "))

polegados, jardas, milhas = converter_medidas(pes)

print(f'{pes} pés equivalem a:')
print(f'{polegados:.2f} polegados')
print(f'{jardas:.2f} jardas')
print(f'{milhas:.2f} milhas')


