# 6. Manipulação de Arquivos em Python 📂
# Python facilita a leitura e escrita de arquivos, permitindo manipular diferentes tipos de dados armazenados em arquivos de texto ou binários.

# Abrindo um Arquivo
# Para abrir um arquivo, usamos a função open(), que recebe o nome do arquivo e o modo de abertura:

# Modos de Abertura
# Modo	Descrição
# "r"	Modo de leitura (read) - erro se o arquivo não existir
# "w"	Modo de escrita (write) - cria ou sobrescreve o arquivo
# "a"	Modo de anexação (append) - adiciona conteúdo ao final
# "r+"	Modo de leitura e escrita sem apagar o conteúdo
# "wb"	Modo binário de escrita
# "rb"	Modo binário de leitura

# Escrevendo em um Arquivo

# Podemos abrir um arquivo no modo "w" para escrever. Se ele já existir, será sobrescrito.
with open("dados.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# 💡 Dica: Usamos \n para quebrar linhas.
# 🔹 O uso do with open(...) garante que o arquivo será fechado automaticamente após o uso.

# Se quisermos adicionar (em vez de sobrescrever), usamos "a" (append):
with open("dados.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada\n")

# Lendo um Arquivo
# Para ler o conteúdo de um arquivo, usamos o modo "r":
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)  # Exibe todo o conteúdo do arquivo

# Lendo linha por linha
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove espaços extras e quebras de linha

# Ou podemos usar readlines() para obter uma lista de linhas:
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)  # Exibe o conteúdo como uma lista

# Manipulação de Arquivos Binários
# Para arquivos como imagens ou PDFs, usamos os modos "rb" e "wb".

# Exemplo: Copiando uma imagem
with open("imagem.jpg", "rb") as origem:
    with open("copia.jpg", "wb") as destino:
        destino.write(origem.read())

# Gerenciando Arquivos e Diretórios
# Python também permite manipular arquivos e diretórios com o módulo os.

# Verificar se um arquivo existe
import os

if os.path.exists("dados.txt"):
    print("O arquivo existe!")
else:
    print("O arquivo não existe.")

# Remover um arquivo
os.remove("dados.txt")

# Criar um diretório
os.mkdir("nova_pasta")

# Listar arquivos de um diretório
print(os.listdir("."))  # Lista arquivos na pasta atual
