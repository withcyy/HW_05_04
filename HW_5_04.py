class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def __str__(self):
        return f"{self.brand} {self.model} - Power: {self.power}W"


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity

    def brew_coffee(self):
        print("Brewing coffee...")


class Blender(Device):
    def __init__(self, brand, model, power, speed_levels):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):
        print("Blending ingredients...")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_type):
        super().__init__(brand, model, power)
        self.blade_type = blade_type

    def grind_meat(self):
        print("Grinding meat...")

coffee_machine = CoffeeMachine("Philips", "HD8827/09", 1450, 1.8)
blender = Blender("Vitamix", "E310", 1380, 10)
meat_grinder = MeatGrinder("KitchenAid", "KSMMGA", 500, "Metal")

print(coffee_machine)
print(blender)
print(meat_grinder)

coffee_machine.brew_coffee()
blender.blend()
meat_grinder.grind_meat()