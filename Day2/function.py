""" For create a function you have to use def and then function name(): """


def sum(a, b):
    result = a+b
    return result


result = sum(12, 34)
print(result)

""" Factorial number """


def fectorial(num):
    if (num == 1 or num == 2):
        return num
    if (num > 2):
        result = num
        for number in range(num):
            result = result*(num-1)
            num = num-1
            if (num == 1):
                break
    return result


fact = fectorial(int(input()))
print(fact)
