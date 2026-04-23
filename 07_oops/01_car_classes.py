class Car:
   def __init__(self, brand,model):
      self.__brand = brand
      # with __variable_name is private
      self.model = model
   def full_name(self):
      # return self.brand + " "+ self.model
      return f"{self.__brand} {self.model}"
   def get_brand(self):
       return self.__brand
   
class ElectricCar(Car):
      def __init__(self,brand,model,battery_size):
          super().__init__(brand,model)
          self.battery_size = battery_size


my_ecar = ElectricCar("Telsla","Model S","85kWh")
# print("My E Car details :: ",my_ecar.brand," ",my_ecar.model," ",my_ecar.battery_size)
# print(my_ecar.__brand)
print(my_ecar.get_brand())
my_car = Car("Toyota","Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata","Punch")
# print(my_new_car.model)