import json

from typing import List

with open("data1.json", "r+") as f:
    data = json.load(f)

print(data)


class Locomotive():
    def __init__(self, mass, max_towable_mass):
        self.mass = mass
        self.max_towable_mass = max_towable_mass

    def __str__(self):
        return f"Locomotive information - mass: {self.mass}, max towable mass: {self.max_towable_mass}"

    def print_info(self):
        print(f'Locomotive - mass: {self.mass}, max_towable_mass: {self.max_towable_mass}')

    @staticmethod
    def load_from_dict(data) -> "Locomotive":
        return Locomotive(mass=data['mass'], max_towable_mass=data['max_towable_mass'])


class Wagon():
    def __init__(self, mass, mass_of_the_load, maximum_mass, unique_wagon_number):
        self.mass = mass
        self.mass_of_the_load = mass_of_the_load
        self.maximum_mass = maximum_mass
        self.unique_wagon_number = unique_wagon_number

    def __repr__(self):
        return f"{self.unique_wagon_number} wagon information - mass: {self.mass}, mass of the load: {self.mass_of_the_load}, " \
               f"maximum mass: {self.maximum_mass}"

    @staticmethod
    def load_from_dict(data) -> "Wagon":
        return Wagon(mass=data['mass'], mass_of_the_load=data['mass_of_the_load'], maximum_mass=data['maximum_mass'],
                     unique_wagon_number=data['unique_wagon_number'])

    def print_info(self):
        print(
            f'Wagon {self.unique_wagon_number} - mass: {self.mass}, mass_of_the_load: {self.mass_of_the_load}, '
            f'maximum_mass: {self.maximum_mass}')


class Train():
    def __init__(self, locomotive: Locomotive, wagons: List[Wagon], train_id):
        self.locomotive = locomotive
        self.wagons = wagons
        self.train_id = train_id

    @staticmethod
    def load_from_json(filename) -> "Train":
        with open(filename, 'r') as f:
            data = json.loads(f.read())
            locomotive = Locomotive.load_from_dict(data['train']['locomotive'])
            wagons = [Wagon.load_from_dict(wagon_data) for wagon_data in data['train']['wagons']]
            train_id = data['train']['train_id']
            train = Train(locomotive=locomotive, wagons=wagons, train_id=train_id)
            return train

    def print_info(self):
        self.locomotive.print_info()
        for wagon in self.wagons:
            wagon.print_info()

    def __repr__(self):
        return f"Train_ID {self.train_id}"


class Station():
    def __init__(self, station_id, trains: list[Train]):
        self.station_id = station_id
        self.trains = trains

    def __str__(self):
        return f"Station number {self.station_id}. Trains which are located in this station: {self.trains}"

    def train_depart(self, train_id):
        decoupled_train = self.trains.pop()
        return decoupled_train

    def train_arrived(self, arrived_train):
        self.trains.append(arrived_train)


locomotive_1 = Locomotive(mass=300, max_towable_mass=2000)
wagon_1_1 = Wagon(mass=20, mass_of_the_load=10, maximum_mass=50, unique_wagon_number=775)
wagon_1_2 = Wagon(mass=40, mass_of_the_load=10, maximum_mass=50, unique_wagon_number=776)
train_1 = Train(locomotive=locomotive_1, wagons=[wagon_1_1, wagon_1_2], train_id=156)
train_1.print_info()

train_2 = Train.load_from_json("data1.json")
train_2.print_info()

locomotive_1 = Locomotive(mass=300, max_towable_mass=2000)
wagon_2_1 = Wagon(mass=20, mass_of_the_load=10, maximum_mass=60, unique_wagon_number=795)
wagon_2_2 = Wagon(mass=40, mass_of_the_load=15, maximum_mass=60, unique_wagon_number=796)
wagon_2_3 = Wagon(mass=50, mass_of_the_load=20, maximum_mass=60, unique_wagon_number=797)
train_3 = Train(locomotive=locomotive_1, wagons=[wagon_2_1, wagon_2_2, wagon_2_3], train_id=123)
train_3.print_info()
# train_3.save_to_json("st1.json")


station_1 = Station(station_id=1, trains=[train_1])
station_2 = Station(station_id=2, trains=[train_3])

departed_train_1 = station_1.train_depart(train_id=156)
print(departed_train_1, "has left!")
# print(departed_train_1.train_id)
station_2.train_arrived(departed_train_1)

print("Station1 has these trains:")
print(station_1.trains)
print("Station2 has these trains:")
print(station_2.trains)

# print(station_1.trains[0].wagons[0].unique_wagon_number)
# print(station_2)
