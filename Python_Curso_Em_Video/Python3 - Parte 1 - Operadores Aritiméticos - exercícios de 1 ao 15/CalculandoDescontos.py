preco = float(input('Qual o preço do produto?: R$'))
desconto = int(input('Qual a porcetagem do desconto?: '))
print('O produto que custava R${}, esta em promoção com {}% de desconto no valor de {}'.format(preco, desconto, (preco - (preco * desconto/100))))