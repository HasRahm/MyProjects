#Name: Hasin Shadab Rahman                                                          #UID:U87513234

import math

class Polygon:
    #Hidden data members to store the number of sides and side length
    #An initializer method to initialize the data members
    def __init__(self):
        self._num_sides = 0
        self._side_length = 0.0
     #Accessor and mutator methods to get/set the data members   
    def get_num_sides(self):
        return self._num_sides
    
    def set_num_sides(self, num_sides):
        self._num_sides = num_sides
        
    def get_side_length(self):
        return self._side_length
    
    def set_side_length(self, side_length):
        self._side_length = side_length
    #Methods to calculate perimeter and area    
    def perimeter(self):
        return self._num_sides * self._side_length
    
    def area(self):
        return (self._num_sides * (self._side_length ** 2)) / (4 * math.tan(math.pi / self._num_sides))

#Creates a Polygon object
#Uses mutator methods to set the polygon's attributes
#Uses accessor methods to display the polygon's dimensions
def main():
    poly = Polygon()
     #Prompts user for number of sides and side length
    #Validates input to ensure valid values are entered
    while True:
        num_sides = int(input("Enter the number of sides (>=3): "))
        if num_sides < 3:
            print("Invalid entry. Re-enter the number of sides (>=3)")
        else:
            break
            
    while True:
        side_length = float(input("Enter the length of each side (>= 0.1): "))
        if side_length < 0.1:
            print("Invalid entry. Re-enter the length of each side (>= 0.1)")
        else:
            break
            
    poly.set_num_sides(num_sides)
    poly.set_side_length(side_length)

    print(f"The polygon has {poly.get_num_sides()} sides. Each side is {poly.get_side_length()} units in length.")
    print(f"The perimeter of the polygon is {poly.perimeter():.3f} units and its area is {poly.area():.3f} square units.")
#Calls the perimeter and area methods to calculate and display results
if __name__ == "__main__":
    main()