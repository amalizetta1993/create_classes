#task 8.1.1
class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    
    #функция определения типа транспорта   
    def get_vehicle_type(self, wheels):
        self.wheels = wheels
        types = {1: "моноколесо",
                 2: "мотоцикл",
                 3: "трицикл",
                 4: "машина"            
                }
        if wheels in types:
            type_transport = f'Это {types[wheels]} марки {self.name}'
        
        return type_transport
    
    #функция получения данных
    def get_data(self):
        return self.name, self.mileage   
    
    #функция, дающая совет по приобритению     
    def get_vehicle_advice(self):
        if self.mileage<=50000:
            advice = f'Неплохо! {self.name} можно брать.'
        elif self.mileage>50000 and self.mileage<=100000:
            advice = f'{self.name} надо внимательно проверить.'  
        elif self.mileage>100000 and self.mileage<=150000:
            advice = f'{self.name} надо провести полную диагностику.'
        else:
            advice = f'{self.name} лучше не покупать.'              
        return advice


transport1 = Vehicle('Hyundai', 17000)
transport2 = Vehicle('Rutrike', 100020)
transport3 = Vehicle('Kawasaki', 165000)
transport4 = Vehicle('KingSong', 65000)


print(transport1.get_vehicle_type(4))
print(transport2.get_vehicle_type(3))
print(transport3.get_vehicle_type(2))
print(transport4.get_vehicle_type(1))

print(transport1.get_vehicle_advice())
print(transport2.get_vehicle_advice())
print(transport3.get_vehicle_advice())
print(transport4.get_vehicle_advice())