# Exercício 01 - Média

# Digita 3 números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Calcula a média
media = (n1 + n2 + n3) / 3

# Mostra o resultado
print("A média é:", media)

# Exercício 02 - Verificar idade

# Digita a idade
idade = int(input("Digite a sua idade: "))

# Verifica se é maior ou menor de idade
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exercício 03 - Calculadora

# Digita os dois números
n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))

# Escolhe a operação
op = input("Informe a operação (+, -, *, /): ")

# Guarda o resultado
calculo = 0

# Verifica qual operação foi escolhida
if op == "+":
    calculo = n1 + n2

elif op == "-":
    calculo = n1 - n2

elif op == "*":
    calculo = n1 * n2

elif op == "/":
    calculo = n1 / n2

else:
    print("Operação inválida.")

# Mostra o resultado
print("Resultado:", calculo)

# Exercício 04 - Aprovação do aluno

# Digita a nota
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Verifica se o aluno foi aprovado
if nota >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
