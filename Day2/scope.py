""" scope is the most important in python, you can access the global varibal from local scope but You can not modify thus """

blance = 3000


def buy_things(items, price,):
    global blance
    blance = blance-price
    return blance


newBlance = buy_things('shart', 700)
print(newBlance)
