# Python Basics

# 1. Instalando o Python
# Baixe e instale pelo site oficial: python.org
# Verifique a instalação:
# python --version  # ou python3 --version

# 2. Sintaxe Básica

# Comentários

# Isso é um comentário de uma linha
""" Isso é um comentário
de múltiplas linhas """

# Variáveis e Tipos de Dados

name = "John Doe" # String
age = 30          # Number (int)
weight = 68.7     # Number (float)
alive = True      # Booleano

# Entrada e Saída

# name = input("Enter your name: ")
# print("Hello", name)

# Operadores Matemáticos

soma = 17 + 3           # Adição
sub = 20 - 2            # Subtração
mult = 19 * 3           # Multiplicação
div = 10 / 2            # Divisão (resultado float)
divInt = 10 // 3        # Divisão inteira
modulo = 10 % 3         # Resto da divisão
expoente = 2 ** 3       # Exponenciação

# 3. Estruturas de Controle

# Condicionais (if, elif, else)
age = 27
if age >= 18:
  print("Maior de idade")
elif age == 17:
  print("Quase lá!")
else:
  print("Menor de idade")

# Laços de Repetição

# While:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# for: 
for i in range(5):  # 0 a 4
    print(i)

# Loop em listas:
nomes = ["Alice", "Bob", "Carol"]
for nome in nomes:
    print(nome)

# 4. Estruturas de Dados

# Listas
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Number:", numbers[2])

# Dicionários
people = {"nome": "Alice", "idade": 25}
print(people["nome"])  # Acessa um valor
people["cidade"] = "São Paulo"  # Adiciona chave/valor

# 5. Funções

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))

# 6. Manipulação de Arquivos

# Escrevendo em um arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, Mundo!")

# Lendo um arquivo
with open("arquivo.txt", "r") as arquivo:
    print(arquivo.read())

# 7. Módulos e Bibliotecas
# Importando módulos

import math
print(math.sqrt(16))  # Raiz quadrada de 16

