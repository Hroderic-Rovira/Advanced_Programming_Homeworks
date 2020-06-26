
class City():

    def __init__(self, city_id, power_consumed, hour_measurement):
        self.city_id = city_id
        self.power_consumed = power_consumed
        self.hour_measurement = hour_measurement

class Substation():

    def __init__(self, substation_name, city_id, total_consumed, peak_hour):
        self.substation_name = substation_name
        self.city_id = city_id
        self.total_consumed = total_consumed
        self.peak_hour = peak_hour

class Operator():
    
    def __init__(self, operator_ID, operator_name):
        self.operator_ID = operator_ID
        self.operator_name = operator_name