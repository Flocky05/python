
num = int(input("Enter how much number :",))
total_sum = 0

for n in range(num):
    numbers = int(input("enter a number: ",))
    total_sum += numbers
avg = total_sum/num
print(avg)
