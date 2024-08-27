"""
Iterando strings com while
"""
#       012345678910
# nome = 'Pedro Dutra'  # Iteráveis
#      1110987654321


nome = 'Tessa Vizani'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)