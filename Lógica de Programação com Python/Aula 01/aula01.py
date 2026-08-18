# ==========================================================
# Aula 01 - Introdução ao Python
# ==========================================================


# ==========================================================
# Exercício 01 - Olá Mundo
# ==========================================================

# Exibindo uma mensagem na tela com meu nome
print("Olá, meu nome é Luis")


# ==========================================================
# Exercício 02 - Sequência de números
# ==========================================================

# Exibindo os números de 1 até 10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)


# ==========================================================
# Exercício 03 - Variáveis
# ==========================================================

# Armazenando o nome
nome = "Luis"

# Armazenando a idade
idade = 33

# Armazenando a cidade
cidade = "Brasília"

# Armazenando o curso
curso = "Inteligência Artificial e Machine Learning"

# Exibindo os valores armazenados
print(nome)
print(idade)
print(cidade)
print(curso)


# ==========================================================
# Exercício 04 - Soma de dois números
# ==========================================================

# Pedindo o primeiro número ao usuário
num1 = int(input("Digite o primeiro número: "))

# Pedindo o segundo número ao usuário
num2 = int(input("Digite o segundo número: "))

# Calculando a soma
soma = num1 + num2

# Exibindo o resultado
print("A soma é:", soma)


# ==========================================================
# Exercício 05 - Operadores Aritméticos
# ==========================================================

# Criando duas variáveis numéricas
num1 = 8
num2 = 4

# Realizando a adição
print("A soma é:", num1 + num2)

# Realizando a subtração
print("A subtração é:", num1 - num2)

# Realizando a multiplicação
print("A multiplicação é:", num1 * num2)

# Realizando a divisão
print("A divisão é:", num1 / num2)

# ==========================================================
# Parte 2 - Strings: Índices e Fatiamento (Slicing)
# ==========================================================

texto = "Python"

# Primeiro caractere
print(texto[0])

# Último caractere
print(texto[-1])


# ----------------------------------------------------------
# Fatiamento (Slicing)
# ----------------------------------------------------------

# Do índice 0 até o índice 2
# O índice final não é incluído
print(texto[0:3])

# Copia a string inteira
print(texto[::])

# Pega os caracteres pulando de 2 em 2
print(texto[::2])

# Inverte a string
print(texto[::-1])

# ==========================================================
# Exercício 06 - Primeiro caractere
# ==========================================================

# Criando a string
texto = "Python"

# Exibindo o primeiro caractere
print(texto[0])


# ==========================================================
# Exercício 07 - Localizando um caractere
# ==========================================================

# Criando a string
texto = "Hello, World!"

# Exibindo o caractere "W"
print(texto[7])


# ==========================================================
# Exercício 08 - Fatiando o início da string
# ==========================================================

# Criando a string
texto = "Data Science"

# Exibindo os três primeiros caracteres
print(texto[0:3])


# ==========================================================
# Exercício 09 - Fatiando o final da string
# ==========================================================

# Criando a string
texto = "Machine Learning"

# Exibindo os três últimos caracteres
print(texto[-3:])


# ==========================================================
# Exercício 10 - Desafio bônus
# ==========================================================

# Pedindo o nome completo ao usuário
nome = input("Digite seu nome completo: ")

# Exibindo a primeira letra do nome
print(nome[0])

# Exibindo o nome invertido
print(nome[::-1])

# Exibindo a quantidade de caracteres do nome
print(len(nome))