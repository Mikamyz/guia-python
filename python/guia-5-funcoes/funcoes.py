# 5. Funções em Python 🔄
# Funções são blocos de código reutilizáveis que ajudam a organizar melhor o programa, tornando-o mais modular e eficiente.

# Criando uma Função
# Para definir uma função em Python, usamos a palavra-chave def:

def saudacao():
  print("Esse é o guia número 5")

#Para chamar a função:
saudacao()

# Funções com Parâmetros
# Podemos passar valores para a função ao chamá-la.

def saudacao(nome):
  print(f"Olá, {nome}!")

saudacao("Maria")  # Saída: Olá, Maria!

# Funções com Retorno
# Uma função pode retornar valores usando return.

def soma(a, b):
  return a + b

resultado = soma(5, 5)
print(resultado)
# Podemos armazenar o retorno em uma variável para usar depois.

# Funções com Múltiplos Retornos
# Uma função pode retornar mais de um valor como uma tupla.

def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

resultado1, resultado2 = operacoes(10, 4)
print(resultado1)  # Saída: 14
print(resultado2)  # Saída: 6
