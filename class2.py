class Transport(object):
    # конструктор
    def __init__(self, name, max_speed, mileage):
        self.name = name;
        self.max_speed = max_speed;
        self.mileage = mileage;
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров";

# Наследуем класс Autobus от Transport
class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return super ().seating_capacity (capacity = 50);
    
Autobus_Liaz = Autobus("Автобус ЛиАЗ-5292", 65, 5250);
print(Autobus_Liaz.seating_capacity());