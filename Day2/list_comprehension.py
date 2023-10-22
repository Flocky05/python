
""" Write a program create a list from other list here will be odd number and not disiable by 5 """
numbers = [8, 10, 45, 35, 48, 15, 65, 3, 13, 46, 95, 23, 65, 15, 26, 24]
odds = []
for num in numbers:
    if (num % 2 == 1 and num % 5 != 0):
        odds.append(num)
print(odds)

# we are use that easy way
odds2 = [num for num in numbers if num % 2 == 1 if num % 5 != 0]
print(odds2)
