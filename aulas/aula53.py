
"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Kathleen'), (1, 'Tessa'), (2, 'Pedro'), (3, 'Noah')]
lista = ['Kathleen', 'Tessa', 'Pedro']
lista.append('Noah')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
