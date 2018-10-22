import mysql.connector

def add_user():
    input_array = []
    user_name = input("Please enter the name of the Agency: ")
    address = input("Please enter the address of the Agency: ")
    number_of_employees = int(input("Please indicate the number of employees in the Agency: "))
    iCARE_Temp_choice = input("Please indicate the choice of the ICARE template: ")
    input_array.append(user_name)
    input_array.append(address)
    input_array.append(number_of_employees)
    input_array.append(iCARE_Temp_choice)
    return input_array
