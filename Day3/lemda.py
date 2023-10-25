# lamda is one kind of small functin declaration procedure ,That means the syntax is like
""" functionName = lambda variale: value """


""" def doubled(num):
    return num*2 """
# thus function can be created by others way like:
def doubled(num): return num*2


print(doubled(2))


actors = [
    {'name': 'sabana', 'age': 56},
    {'name': 'sibla', 'age': 20},
    {'name': 'Sakib Khan', 'age': 51},
    {'name': 'Purnima', 'age': 45},
    {'name': 'Suhasini', 'age': 21},
]

juniors = filter(lambda actor: actor['age'] < 21, actors)
print(list(juniors))
