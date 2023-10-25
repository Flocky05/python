""" For create a file and write something in the file """
with open('message.text', 'w') as file:
    for i in range(7):
        file.write("Who are you bro?\n")

with open('message.text', 'a') as file:
    file.write('My name is Rakibul Islam')

"""  for read the file """
with open('message.text', 'r') as file:
    content = file.read()

print(content)
