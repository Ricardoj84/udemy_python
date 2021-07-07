import math
print('Digite o valor de 2 catetos de um triangulo:')
catetoa = float(input())
catetob = float(input())
hipotenusa = math.sqrt(catetoa**2+catetob**2)
print(f'O valor da hipotenusa do triangulo e: {hipotenusa}')
