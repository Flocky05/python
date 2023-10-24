""" a dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. """
person = {'name': 'Rakibul', 'address': 'Tangail',
          'Education': 'Dhaka University', 'Job': 'Work less'}
print(person)
print(person['Job'])
person['Language'] = 'python'
print(person)
print(person.values())
print(person.keys())

""" we can also create nested dictionary """
friend = {'id': {'name': 'mehedi', 'address': 'BagerHat', 'versity': 'FUET'},
          'father_Name': 'Momen Khan', 'Mother_Name': 'Johura Begum'}
print(friend)
del friend['father_Name']
print(friend)
