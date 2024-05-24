#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        self.size = size
        self.condition = "New" 

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New" 

class TestShoe:
    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "The shoe has been repaired."
