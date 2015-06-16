__author__ = 'aluno01'

import random

#random de numeros inteiros
print(random.randint(0, 5))

#embaralhar itens do array
numeros = [1, 3, 5, 7, 9]
random.shuffle(numeros)
print(numeros)

#random de float de 0 a 1
print(random.random())

#random float com meta, no caso de 6 a 11
print(random.uniform(6, 11))

#escolhe um elemento aleatorio em uma string
print(random.choice('abcdefghijklmnopqrstuvwxyz'))

#seleciona aleatoriamente um numero X de elementos
print(random.sample(numeros, 3))