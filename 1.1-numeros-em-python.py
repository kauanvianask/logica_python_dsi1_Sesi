# AULA COMPLETA: NUMEROS EM PYTHON 
"""""
vamos aprender: 
1 - tipos numericos
2 - conversões de tipos
3 - hierarquia numérica
4 - opercaões matemáticas
5 - coerção de tipos 
6 - verificação de tipos 
7- entrada de dados
"""
# ===========================
# PASSO 01 - TIPOS NUMÉRICOS 
# ===========================
# int -> interios 
# float -> com casas decimais 
# complex -> complexos (usado em matemática/engenharia)

print ("===== TIPOS NUMÉRICOS =====")

# EXEMPLOS 01 - NUMERO INTEIRO 

# criamos uma variável chamada numero_inteiro
numero_inteiro = 10 

# mostramos o valor
print ("Valor:" , numero_inteiro)

# Type() mostra qual é o tipo da variável
print ("Tipo:", type(numero_inteiro))

print ("--------------------------------------------------------")

#  EXEMPLO 02 - NUMERO DECIMAL

# Criamos uma variável
numero_decimal = 3.14

# mostramos o valor
print ("Valor:" , numero_decimal)

# Type() tipo da variável 
print ("Tipo:" , type(numero_decimal))

print ("--------------------------------------------------------")

# EXEMPLO 03 - NUMERO COMPLEXO

# Possui duas partes
# Parte real (Numero normal)
# Parte imaginária (multiplicada por j)

# Estrutura Geral:
# numero = a + bj 

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j 

print ("Valor:" , numero_complexo)

# Type() tipo da variável
print ("Tipo:" , type(numero_complexo))

print ("--------------------------------------------------------")

#EXEMPLO 04 - ACESSANDO CADA PARTE DO NÚMERO

#.real retorna a parte real
print("Parte Real: ", numero_complexo.real)

#.imag RETORNA A PARTE IMAGINÁRIA
print("Parte imaginária:", numero_complexo.imag)
#apenas para separar visualmente no terminal 
print("\n")

#===============================
## passo 02 - conversão tipos 
#===============================

#exemplo classico
##dados vindos do usuário são texto (string), muitas vezes é necessario converter eles.

print ("===== Conversões =====")

# float -> int

valor = int(3.9)
print ("int(3.9):", valor)
print ("tipo:", type(valor))

print ("--------------------------------------------")

#string -> int

valor1 = "10"
print (type(valor1))

valor2 = int ("10")
print('int ("10"):', valor2)
print ("tipo: ", type(valor2))

print ("--------------------------------------------")

#int -> float

valor3= float(10)
print ("float (10): ", valor3)
print ("tipo: ", type(valor3))
