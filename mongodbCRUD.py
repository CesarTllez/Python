from pymongo import MongoClient #If you don't have this -> pip install pymongo
import pandas as pd #If you don't have this -> pip install pandas

#Athlas host. Enter the URL provided by mongodb atlas.
CONNECT_STRING = "mongodb+srv://your_user:your_password@cluster0.2ijgn.mongodb.net/test" #<- Example
#Mongo cursor
client = MongoClient(CONNECT_STRING)
#Create data base
dataBase = client['database_name']
#Create collection
collection = dataBase['collection_name']

while True:

    option = int(input('\nWhat do you want to do?'
              +'\n1. Register student.'
              +'\n2. See all records.'
              +'\n3. Update student.'
              +'\n4. Delete student.'
              +'\n5. Exit.'
              +'\n\Enter the corresponding number: '))
    print('\n')

    #Create document.
    if option == 1:
        student = {
            'name': input('Enter name: '),
            'last_name': input('Enter last name: '),
            'code': int(input('Enter code: ')),
            'state': int(input('Enter state (1. Studying.\n2. Retired.\nEnter the corresponding number: )'))
        }

        if student['state'] == 1:
            student['state'] = True
        else:
            student['state'] = False

        collection.insert_one(student)
    
    #See all documents.
    if option == 2:
        #If you don't want to use Pandas.
        #for document in collection.find():
        #    print(document)

        dataFrame = pd.DataFrame(collection.find())
        print(dataFrame)

    #Update document.
    if option == 3:
        student = {
            'code': int(input('Enter code: ')),
            'state': int(input('Enter state (1. Studying.\n2. Retired.\nEnter the corresponding number: )'))
        }

        if student['state'] == 1:
            student['state'] = True
        else:
            student['state'] = False

        collection.update_one({'code': student['code']}, {'$set': {
            'state': student['state']
        }})

    #Delete document.
    if option == 4:
        code = int(input('Enter code: '))
        collection.delete_one({'code': code})

    #Exit app.
    if option == 5:
        break