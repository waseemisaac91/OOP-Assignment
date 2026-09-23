class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
    def area(self):
        result = self.width * self.height
        return result
    def perimeter(self):
        result1= (self.width + self.height) * 2
        return result1

    
# Create an object
rectangle = Rectangle(5, 7)

# Print area and perimeter
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())