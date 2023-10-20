""" If else  is one of the common conditional statement , normaly we use that when one codition needed further more codition is needed that time we use elseif but in python we cannot use elseif here we use elif """

""" Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill """

a = int(input('enter the unit charges that is you used: '))
if (a < 50):
    print('You have to pay: ', a*0.5)
elif (a <= 150):
    print('You have to pay: ', a*0.75)
elif (a <= 250):
    print('You have to pay: ', a*1.20)
elif (a <= 500):
    print('You have to pay: ', a*1.50)
else:
    print('You have to pay: ', (500*1.50)+((a-500)*.2))
