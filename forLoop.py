""" As we can't use comma(,),semicolone(;) so for loop will others way, the syntax are for loop like:
for arrayelementName in arrayName:

 """
students = ['rakib', 'sakib', 'adnan', 'tipu', 'mehedi', 'emon', 'shanto']

for student in students:
    print(student)

""" Range if you want to print out natural number may u use range(statr,end) """

for number in range(1, 10):
    print(number)

"""  Write a Python program to compute the sum of the first 10 natural numbers. """
sum = 0
for i in range(1, 11):
    sum = sum+i
print('sum of first 10 natural numbers are: ', sum)

x = 5
y = 3
print('The mod is of the number', x % y)

x = 10
y = 2
print(x // y)
