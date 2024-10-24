import os

# Definindo o nome do arquivo
filename = "alegria.txt"

# Criando e escrevendo no arquivo
with open(filename, "w") as file:
    file.write("Só alegria hahaha")

print(f"Arquivo '{filename}' criado e editado com sucesso!")