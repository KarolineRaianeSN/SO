"""Alunos: Caius Vinicus e Karoline Raiane"""

import os

nome_arquivo = input('Digite o nome do arquivo: ')
print('Arquivo criado com sucesso!')
with open(nome_arquivo, "w") as file:
    file.write("Só alegria hahaha")
print('"Só alegria hahaha" foi inserido no arquivo com sucesso!')