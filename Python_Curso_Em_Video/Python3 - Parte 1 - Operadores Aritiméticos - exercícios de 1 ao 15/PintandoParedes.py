largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}mx{}m. Logo a área é de {:.2f}m²'.format(largura, altura, area))
print('Para pintar sua parede, você precisará de {}l de tinta'.format(area/2))