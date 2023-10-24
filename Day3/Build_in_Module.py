from math import *
from random import *
from time import *
result = ceil(4.7)
number = round(343.34)
print(result, number)
x = [12, 1, 2, 3, 4, 5, 6, 32, 21, 23, 34, 45, 45, 56, 54, 43, 32]
num = random()
print('This is random number: ', round(num*10))
print('The winner is : ', choice(['sakib', 'rakib', 'niloy', 'sobuj',
      'mehedi', 'emon', 'milon', 'rohan']))
""" shuffle() inside of shuffle use a array, at frist you have careate a array and put some value and use shuffle module and then call the array """
shuffle(x)
print(x)
sleep(0.5)
# sample(arrayName, how much element do you want show)
print(sample(x, 7))
# it is also a rendom number
print(uniform(2, 3))
print(triangular(12, 13, 8))
