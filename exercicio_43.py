valortotal = int(input("Digite o valor total da compra: "))
desconto = valortotal*0.9
parcela = valortotal/3
comissaovista = desconto*5/100
comissaoparcelada = valortotal*5/100

print(f"Valor a vista: {desconto}")
print(f"Parcelado em 3x, parcela de: {parcela}")
print(f"Comissao a vista pro vendedor: {comissaovista}")
print(f"Comissao parcelada pro vendedor: {comissaoparcelada}")

