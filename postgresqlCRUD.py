import psycopg2 as pc2 #If you don't have this -> pip install psycopg2
import pandas as pd #If you don't have this -> pip install pandas

#Connect to database.
connectionDB = pc2.connect(
    database = "database name", 
    user = "postgres", 
    password = "your password",
    host = "localhost",
    port = "5432")

#Create cursor to execute SQL commands.
cursor = connectionDB.cursor()

#Create SQL commands.
sqlCommands = {
    'insertSQL': 'INSERT INTO employees (first_name, last_name, age, email) VALUES (%s, %s, %s, %s)',
    'selectAllSQL': 'SELECT * FROM employees',
    'updateSQL': 'UPDATE employees SET first_name = %s, last_name = %s, age = %s, email = %s WHERE id = %s',
    'deleteSQL': 'DELETE FROM employees WHERE id = %s'   
}

while True:

    option = int(input('\nWhat do you want to do?'
              +'\n1. Register employee.'
              +'\n2. See all records.'
              +'\n3. Update employee.'
              +'\n4. Delete employee.'
              +'\n5. Exit.'
              +'\n\Enter the corresponding number: '))

    if option == 1:
        #Columns values.
        firstName = input('Enter your first name: ')
        lastName = input('Enter your last name: ')
        age = input('Enter your age: ')
        email = input('Enter your email: ')

        #Tuple with the columns values.
        data = (firstName, lastName, age, email)

        #Use the execute method of the cursor to run the SQL command.
        cursor.execute( sqlCommands['insertSQL'], data )
        connectionDB.commit()

        print('User successfully registered in the database.')

    if option == 2:
        #Use the execute method of the cursor to run the SQL command.
        cursor.execute( sqlCommands['selectAllSQL'] )

        #***********************************Optional step****************************************
        #To see the data as a table by console, a dataFrame from the Pandas library will be used.
        #If you don't want to use "Pandas", you can see the table in the following way.
        #->for row in cursor:
        #->    print(row)

        #Define the column names corresponding to the table
        columnNames = ['ID', 'First_Name', 'Last_Name', 'Age', 'Email']

        #Create a dataframe from the "Pandas" library.
        #As first value the data and as second value the columns.
        dataFrame = pd.DataFrame(cursor, columns=columnNames)

        print(f'\n{ dataFrame }\n')

    if option == 3:
        #Columns values.
        firstName = input('Enter another first name: ')
        lastName = input('Enter another last name: ')
        age = input('Enter another age: ')
        email = input('Enter another email: ')
        id = int(input("Enter employee's id to update: "))

        #Tuple with the columns values.
        data = (firstName, lastName, age, email, id)

        #Use the execute method of the cursor to run the SQL command.
        cursor.execute( sqlCommands['updateSQL'], data )
        connectionDB.commit()

        print('It was updated successfully.')

    if option == 4:
        #Id to delete employee.
        id = int(input("Enter employee's id to delete: "))

        #Use the execute method of the cursor to run the SQL command.
        cursor.execute( sqlCommands['deleteSQL'], [id] )
        connectionDB.commit()

    if option == 5:
        break

connectionDB.close()