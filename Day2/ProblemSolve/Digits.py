
i = int(input())

while i > 0:
    i = i-1
    m = int(input())
    while m > 0:
        re = m - m % 10
        print(m % 10, end=" ")
        m = int(re/10)
