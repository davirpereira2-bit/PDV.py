preco_unitario = 7.0

quantidade = int(input('Digite a quantidade de produtos:'))

preco_total = preco_unitario * quantidade
print(f'o preço total do produto é: {preco_total}')

valor_pago = float(input('Digite o valor pago:'))

if valor_pago < preco_total:
    print('Valor insuficiente para pagamento.')
    resto = preco_total - valor_pago

    print(f'falta R$ {resto} para completar o pagamento')
elif valor_pago > preco_total:
    troco = valor_pago - preco_total
    print(f'o troco é: R$ {troco}')

else:
    print('pagamento realizado com sucesso, sem troco.')
