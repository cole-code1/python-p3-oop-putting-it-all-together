#!/usr/bin/env python3

class Shoe:

    def __init__(self,brand,size):
        self.size = size
        self.brand = brand
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


shoe = Shoe("Nike", 10)  # Create a new Shoe object
print(shoe.size)  # Access size, will call the getter
print(shoe.brand)
shoe.size = 12  # Use the setter to set a new size
shoe.cobble()  # Call the cobble method
