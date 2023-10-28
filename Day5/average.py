num = int(input("Enter the number: ",))
total_sum = 0
for i in range(num+1):
    total_sum = total_sum+i
    i = i+1
average = total_sum/num
print(average)
