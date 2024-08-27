"""
Exercício
Exiba os índices da lista
0 Kathleen
1 Tessa
2 Pedro
"""
lista = ['Kathleen', 'Tessa', 'Pedro']
lista.append('Noah')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))