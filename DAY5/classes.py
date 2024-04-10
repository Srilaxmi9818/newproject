class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def describe(self):
        print("Rectangle Description:")
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

# Example usage:
# Create a Rectangle object
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(8, 4)

# Calculate and print the area of the rectangle
print("Area of the rectangle:", rectangle1.area())

# Print the description of the rectangle
rectangle1.describe()
rectangle2.describe()

