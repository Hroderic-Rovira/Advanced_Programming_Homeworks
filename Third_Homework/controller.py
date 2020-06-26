from model import *
from view import *
import re
import sqlite3 as db_object
import csv
from sqlite3 import Error

#region DataBase Connection String and CRUD functions.
def sql_create_database():
    try:
        connection = db_object.connect("db_ICE.db")
        return connection

    except Error:
        print(Error, "An error has ocurred, the database was not created.")

def sql_create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tbl_Operators(name TEXT)") # A sigle table containing the name of the operator and an autogenerated ID field.
        connection.commit()
    except Error:
        print(Error, "An error has ocurred and the table was not created.")

def sql_insert_row(connection, values):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tbl_Operators(name) VALUES(?)", [values])
        connection.commit()
    except Error:
        print(Error, "An error has ocurred, the data could not be added.")

def sql_list_rows(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM tbl_Operators")
        obj_result = cursor.fetchone()
        connection.commit()

        return obj_result

    except Error:
        print(Error, "An error has ocurred, the table could not be read.")

#endregion

#region Controllers

class Operator_Controller:

    def __init__(self):
        self.obj_operator_view = Operator_View()
        self.obj_substation_view = Substation_View()
        self._city_list = []

    def run(self): # Root function. This is where the programm is going to be running.
        running = True
        userInput = None
        obj_connection = sql_create_database()
        sql_create_table(obj_connection)
        result = sql_list_rows(obj_connection)

        while running == True:
            try:
                if userInput == None:
                    if result: # If there's already a name in the database.
                        self.obj_operator_view.welcome_message(result[0])
                    else: # If there isn't anything in the database.
                        self.obj_operator_view.user_not_found()
                        values= input()
                        sql_insert_row(obj_connection, values)
                        result = sql_list_rows(obj_connection)
                        self.obj_operator_view.user_registration(result[0])

                    if result: # Check if the user wrote its name.
                        self.obj_substation_view.substation_registration()
                        substation_name = input()
                        if substation_name: #Checks if the user wrote a name for the substation.
                            self.obj_substation_view.substation_creation(substation_name)
                            print(self.obj_substation_view.breakliner)
                            Substation_Controller.read_file(self, self._city_list)
                            City_Operator.calculate_info(self, self._city_list)
                        else:
                            self.run()

                        # Here the user decides if he/she wants to generate the report again, or stop the programm.

                        print(self.obj_substation_view.breakliner)
                        self.obj_operator_view.repeat_loop_message()
                        userInput = input()

                        if userInput == 'N':
                            self.obj_operator_view.closing_programm_message()
                            running = False

                        else:
                            self.run()
                    else:
                        self.run()

            except Error:
                print(Error, "An error has ocurred, the programm has been stopped abruptly.")
            except ValueError:
                print(Error, "You have entered a wrong value.")

class Substation_Controller:

    def read_file(self, city_list):# Function used to read or write a .csv file.
        try:
            with open("mediciones.csv", "r") as consumo_data:
                result = csv.reader(consumo_data)
                for item in result:
                    values = str(item).split(';')

                    #Regular expression used to clean the information stored in the list.
                    values = re.findall("\d+",values[0]),re.findall("\d+",values[1]),re.findall("\d+\.?\d+?",values[2])
                    city_list.append(values)
        except:
            print("An error has ocurred, the file could not be read.")

class City_Operator:

    def calculate_info(self, city_list): #This function will calculate the peak hour and the total energy consumed by city.

        _cities = [] # Stores the ID of every city, it won't save duplicated IDs.
        _current_number = 0 # It allowes the code to keep control of the current variable to check if the number already exists in the list.

        _total_energy = 0.00 # Stores the ammount of energy consumed by each city.

        _temp_variable = 0.00 # It helps the code determine which hour was the the hightest.
        _peak_hour = 0 # Stores the hour with the highest consumption value.

        obj_city_view = City_View()

        obj_city_view.city_report_message()

        for item in city_list:
            _current_number = item[1]
            if _current_number not in _cities:
                _cities.append(_current_number)
        for ID in _cities:
            for row in city_list:
                if ID == row[1]:

                    _total_energy += float(str(row[2]).replace("'","").strip('[').strip(']'))

                    if float(str(row[2]).replace("'","").strip('[').strip(']')) > _temp_variable:
                        _peak_hour = row[0]

            obj_city_view.city_report_generated(ID, _total_energy, _peak_hour)
            _temp_variable = 0
            _peak_hour = 0
            _total_energy = 0.00


#endregion

# ## # Investigate what this is # ## #
if __name__ == "__main__":
    control = Operator_Controller()
    control.run()