from vehicles import * 

v1= Vehicle("hannah",4)
v2 = Vehicle("alex",2, location = (3,5), direction = (1, 4), owner = "Alex")

v1.print_info()
print("\n")
v2.print_info()
v2.set_direction(3,5)
v2.location = (20,20) # Inconsistent way to change attributes - not good
print("\n---Alex after changing: \n")
v2.print_info()
v2.base_move(1500)
v2.print_info()


c1 = Car("Ruth", 4, location = (3,5), direction = (1, 4), owner = "Ruth", fuel_capacity = 20, mpg = 50, fuel_level = 15) 

c1.print_info()
c1.move(120)