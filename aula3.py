print ("--------------------------------------------------")
print("Aula sobre escrita em python")

# - Criação de strings
# - String multilinha
# - indices e slices
# - operações com strings
# - imutabilidade
# - metodos uteis
# - formatação de texto
# - unicode e bytes

#-----------------------------------
# 1) Criação de strings
#-----------------------------------

# Strings são textos em python.
# Podem ser criadas usando aspas simples ou duplas

string1 = "python"
string2 = 'Curso de python'
string3 = "Copa 'padrao fifa'"
string4 = 'Copa "padrao fifa"'

print (string1)
print (string2)
print (string3)
print (string4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escaoar caracteres

#-----------------------------------
# 2) Strings multilinha
#-----------------------------------

# Usando três apas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print (menu)

# Esse formato é muito usado para:
# - Menus
# - Documentação
# - Textos longos

#-----------------------------------
# 3) Concatenação automatica
#-----------------------------------

#Quando duas strings aparecem lado a lado, o python junta automaticamente

string = ("Copa " "2026" " Neymar é show mesmo?" " SIM")

print (string)

#-----------------------------------
# 4) Strings como sequencias
#-----------------------------------

#  Uma string funciona como uma sequencia de caracteres, cada caractere possui um indice

st = "maracanã"

print ("Primeira letra:", st [0])

# Só exibir a letra: m

print ("ultima letra:", st [-1])

print ("Trecho 1:4:", st [1:4])

print ("Do inicio até 3:", st [:3])

print ("Do 2 até o fim:", st [2:])

print ("Tamanho", len (st))