#!/usr/bin/env python
"""

A linha acima é usada para executar como script.
Utilizar chmod u+x nomeDoArquivo

"""


__author__ = 'Johan'


#NAO USAR CARACTERES ESPECIAIS! VALEU, FALOU!
frase = "Nos estamos todos bebados, bebados de cair"
print("Original: " + frase)
print("0 a 5 posicao: " + frase[:5])
print("ultimas 4: " + frase[-4:])

#sustenido para comentario em linha
#a funcao len() retorna um inteiro com o tamanho de algo
tamanhoFrase = len(frase)
print("Tamanho da frase: " + str(tamanhoFrase))
#A frase acima precisou ser convertida de inteiro para String
#Para converter inteiro em String: str()
#Para converter String em inteiro: int('')
'''E podemos usar 3 aspas simples ou duplas para comentario em bloco'''

#O if/elif/else ira executar o que esta dentro da indentacao
nome = "Johan"
if nome is "Johan":
    print(nome+" fez este tutorial bem explicado :v")
elif nome is "Kugra":
    print(nome + " e' um apelido.")
else:
    print(nome + " nao registrado como uma opcao valida")

idade = 22
if idade < 20:
    print("Idade menor que 20")
else:
    print("Idade maior que 20")


#array
frutas = ["maca", "banana", "melancia"]
#adicionar item
frutas.append("abacate")
print("Itens no array listados por um FOR")

#Assim como o if/elif/else tudo que estiver endentado dentro do FOR sera executado
for i in frutas:
    print(i)
    print(len(i))

#limitando o for ate a posicao 2
for f in frutas[:2]:
    print(f)
#for 0 a 10
for x in range(10):
    print(x)
#for 5 a 10
for x in range(5,10):
    print(x)
#for 2 a 20 com incremento de 2
for x in range(2,20,2):
    print("For com incremento de 2: ",x)
#while
ctrlLaco = 5
while ctrlLaco <= 10:
    print("While: "+str(ctrlLaco))
    ctrlLaco+=1

magicNum = 26
#percorre de 0 a 101
for n in range(101):
    #se n for igual ao magicNum, o numero e' printado
    if n is magicNum:
        print("Magic num: ",n)
        break
    else:
        print(n)


numContidos = [2, 5, 12, 15, 17]
print("Numeros disponiveis: ",numContidos)
#For de 1 a 20
for n in range(1, 20):
    if n in numContidos:
        #Se o numero N for igual a algum dos numContidos o laco deve continuar mas nao vai printar os numContidos
        continue
    print(n)

#String format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

#Calculos complexos
l = 3 + 4j
print(l)
j=2+l-2j
print(j)

#Bhaskara
a=2
b=2
c=2
from math import sqrt
x1=-(b)+(sqrt(b^2)-4*a*c)/(2*a)
x2=-(b)-(sqrt(b^2)-4*a*c)/(2*a)
print("Valor de x1:", x1)
print("Valor de x2:", x2)