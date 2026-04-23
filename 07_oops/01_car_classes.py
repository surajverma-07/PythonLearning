class Car:
   car_count = 0
   def __init__(self, brand,model):
      self.__brand = brand
      # with __variable_name is private
      Car.car_count += 1
      self.__model = model
   def full_name(self):
      # return self.brand + " "+ self.model
      return  f"{self.__brand} {self.__model}"
   def get_brand(self):
       return self.__brand
   def fuel_type(self):
       return "Petrol or Dieasal"
   @staticmethod
   def general_desc():
       return "Static method it is "
   # property used to make the variable readable only and we can access the fn as a property 
   @property
   def model(self):
       return self.__model
       
class ElectricCar(Car):
      def __init__(self,brand,model,battery_size):
          super().__init__(brand,model)
          self.battery_size = battery_size
      
      def fuel_type(self):
          return "Electric Charge"

my_ecar = ElectricCar("Telsla","Model S","85kWh")
# print("My E Car details :: ",my_ecar.brand," ",my_ecar.model," ",my_ecar.battery_size)
# print(my_ecar.__brand)
# print(my_ecar.get_brand())
# print(my_ecar.fuel_type())

my_car = Car("Toyota","Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata","Punch")
# print(my_new_car.model)
# print(my_new_car.fuel_type())
# my_new_car.model = "Nexon"
print(my_new_car.model)

# print("Total Cars :: ",Car.car_count)
# print(Car.general_desc())

# print(isinstance(my_ecar,ElectricCar))
# print(isinstance(my_ecar,Car))
# print(isinstance(my_car,Car))
# print(isinstance(my_car,ElectricCar))

class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"

class EvCar(Battery,Engine,Car):
    pass

my_ev = EvCar("tata ev","harrier ev")
print(my_ev.engine_info())
print(my_ev.battery_info())