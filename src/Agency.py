import mysql.connector
from mysql.connector import MySQLConnection, Error


def add_agency():
    input_array = []
    # User inputs the necessary fields needed to create an agency
    agency_name = input("Please enter the name of the Agency: ")
    address = input("Please enter the address of the Agency: ")
    number_of_employees = int(input("Please indicate the number of employees in the Agency: "))
    iCARE_Temp_choice = input("Please indicate the choice of the ICARE template: ")
    input_array.append(agency_name)
    input_array.append(address)
    input_array.append(number_of_employees)
    input_array.append(iCARE_Temp_choice)
    return input_array

def main():

    mydb = mysql.connector.connect(user='root', password='newpass123', host='localhost')
    mycursor = mydb.cursor()


    # count = 0
    # while True:
    #     # Create the table
    #     mycursor.execute("CREATE DATABASE testdb")
    #     # Add the necessary columns to the table
    #     mycursor.execute("CREATE TABLE testdb.Agency (agencyID int NOT NULL, name varchar(100) NOT NULL, address varchar(200), number_of_employees int, iCARE_Temp_choice varchar(100))")
    #     if count == 0:
    #         break


    user_input = add_agency()
    agency_name = user_input[0]
    address = user_input[1]
    number_of_employees = user_input[2]
    iCARE_Temp_choice = user_input[3]

    mycursor.execute("INSERT INTO testdb.Agency (name, address, number_of_employees, iCARE_Temp_choice) VALUES (Donald, Street, 400, temp) ")






if __name__ == '__main__':
    main()
