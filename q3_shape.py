
#Question 4 - Shape - by Waseem 

class Shape:
    """Base class for all shapes."""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Default area - to be overridden."""
        return 0
    
    def description(self):
        return f"This is a {self.name} shape."
    
    def __str__(self):
        return self.description()


class Rectangle(Shape):
    """Rectangle shape."""
    
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def description(self):
        return (f"This is a {self.name} shape with "
                f"length {self.length} and width {self.width}.")

class Square(Shape):

    def __init__(self,side):
        super().__init__("Square")
        self.side=side

    def area(self):
        return self.side *self.side
    def description(self):
        return (f"This is a {self.name} shape with Side {self.side} ")

# ---------- Testing ----------
if __name__ == "__main__":

    r = Rectangle(5, 10)
    s =  Sqaure(6)
    
    print(f"Area of {r.name}: {r.area():.2f}")
    print(f"Area of {s.name}: {s.area():.2f}")
 
    print(r.description())
    print(s.description())