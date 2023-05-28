# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: JSON Encoder Decoder
# Version: 1.0: Base version by author
import json

system_msg = """What can I do for you?
    1: Produce a JSON String describing a Vehicle
    2: Decode a JSON String into Vehicle Data
Your Choice: """


# Define Vehicle Model Data
class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass


# Encode Vehicle Data
class MyEncoder(json.JSONEncoder):
    def default(self, w, z=None):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self)


# Decode Vehicle Data
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decoder)

    @staticmethod
    def decoder(d):
        return Vehicle(**d)


if __name__ == '__main__':
    try:
        selection = int(input(system_msg))
        input_registration_number = None
        input_year_of_production = None
        input_passenger = None
        input_mass = None
        if selection == 1:
            try:
                input_registration_number = input('Registration Number: ')
            except TypeError:
                print('Error in Registration Number.')
            try:
                input_year_of_production = int(input('Year of Production: '))
            except TypeError:
                print('Error in Year of Production.')
            input_passenger = input('Passenger [Y/N]: ')
            if input_passenger == 'Y':
                input_passenger = True
            elif input_passenger == 'N':
                input_passenger = False
            else:
                print('Error in Passenger.')
                raise TypeError
            try:
                input_mass = float(input('Vehicle Mass: '))
            except TypeError:
                print('Error in Vehicle Mass.')
            vehicle_data = Vehicle(input_registration_number, input_year_of_production, input_passenger, input_mass)
            json_string = json.dumps(vehicle_data, cls=MyEncoder)
            print('Resulting JSON String is: \n', json_string)
            print('Encoding has been Completed.')
        elif selection == 2:
            try:
                input_json_string = input('Enter Vehicle JSON String: ')
                json_string = input_json_string
                vehicle_data = json.loads(json_string, cls=MyDecoder)
                print(vehicle_data.__dict__)
                print('Decoding has been Completed.')
            except TypeError:
                print('Error in JSON String.')
        else:
            raise TypeError
    except TypeError:
        print('Error in your Input. Please re-run the System.')
