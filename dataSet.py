from random import randint
import pandas as pd #If you don't have this -> pip install pandas

alphabet = 'ABCDEFGHIJKLMÑOPQRSTUVWXYZ'
people = {
    'Name': [],
    'Age': [],
    'Email': []
}
domains = ['gmail', 'hotmail', 'yahoo']

for letter in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            name = (letter+letter2+letter3)
            people['Name'].append(name.capitalize())
            people['Age'].append(randint(1, 100))
            people['Email'].append(
                name.lower()+
                format(randint(1, 99))+
                f'@{domains[randint(0, 2)]}.com')

dataFrame = pd.DataFrame(people)
print(dataFrame)