dias = int(input('Por quantos dias você quer alugar o carro?: '))
km = float(input('Quantos KM pretende percorrer?: '))
print('Percorrendo {}km por {} dias, valor do aluguel ficará em torno de R${}!'.format(km, dias, ((dias * 60) + (km * 0.15))))