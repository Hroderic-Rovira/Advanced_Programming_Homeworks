from model import Substation

class Operator_View:

    def __init__(self):
        self.breakliner =         "|----------------------------------------------|"

    def welcome_message(self, name):
        print(self.breakliner+'\n'+"          Welcome back, {}.".format(name))

    def user_not_found(self):
        print('\n'+"Welcome to the Energy Consumption Calculator System. Please enter your name: ")

    def user_registration(self, name):
        print('\n'+"Excellent, {}.".format(name))

    def repeat_loop_message(self):
        print('\n'+"Would you like you repeat the report? (Y/N)")

    def closing_programm_message(self):
        print(self.breakliner+'\n'+"Thanks for using our application."+'\n'+self.breakliner)
class Substation_View:

    def __init__(self):
        self.breakliner = "|----------------------------------------------|"

    def substation_registration(self):
        print(self.breakliner+'\n'+"Please, enter the name of the substation that your are stationed at:" )

    def error_create_substation(self):
        print('\n'+"An error has ocurred, please make sure you wrote a valid name."+'\n'+self.breakliner)

    def substation_creation(self, name):
        print('\n'+"The substation {} was succesfully created! ".format(name))

class City_View:

    def __init__(self):
        self.breakliner = "|----------------------------------------------|"
    
    def city_report_message(self): 
        print('\n'+"The following report was generated: "'\n')

    def city_report_generated(self, city_id, total_consumed, peak_hour):
        print("City ID:{}, Total Energy Consumed:{}, Peak Hour:{}".format(city_id, total_consumed, peak_hour))

    def error_message(self):
        print('\n'+"Please read the instructions carefully!!")
