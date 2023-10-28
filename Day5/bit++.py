number = int(input())
count = 0
for n in range(number):
    string = str(input())
    if (string[0] == "+" or string[len(string)-1] == "+"):
        count += 1
    if (string[0] == "-" or string[len(string)-1] == "-"):
        count -= 1
print(count)
