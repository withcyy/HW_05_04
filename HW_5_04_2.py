class Ship:
    def __init__(self, name, displacement, length):
        self.name = name
        self.displacement = displacement
        self.length = length

    def __str__(self):
        return f"{self.name} - Displacement: {self.displacement} tons, Length: {self.length} meters"


class Frigate(Ship):
    def __init__(self, name, displacement, length, num_missiles):
        super().__init__(name, displacement, length)
        self.num_missiles = num_missiles

    def fire_missile(self):
        print("Firing missiles...")


class Destroyer(Ship):
    def __init__(self, name, displacement, length, num_cannons):
        super().__init__(name, displacement, length)
        self.num_cannons = num_cannons

    def fire_cannon(self):
        print("Firing cannons...")


class Cruiser(Ship):
    def __init__(self, name, displacement, length, num_torpedoes):
        super().__init__(name, displacement, length)
        self.num_torpedoes = num_torpedoes

    def launch_torpedo(self):
        print("Launching torpedoes...")

frigate = Frigate("Oliver Hazard Perry-class", 4100, 135, 8)
destroyer = Destroyer("Arleigh Burke-class", 9200, 155, 90)
cruiser = Cruiser("Ticonderoga-class", 9600, 173, 8)

print(frigate)
print(destroyer)
print(cruiser)

frigate.fire_missile()
destroyer.fire_cannon()
cruiser.launch_torpedo()