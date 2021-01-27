class Rectangle:

    def __init__(self, width, height):
        # rectangle has two parameters, width and height
        self.width = width
        self.height = height

    def set_width(self, width):
        # use to change the width of the rectangle
        self.width = width

    def set_height(self, height):
        # use to change the height of the rectangle
        self.height = height

    def get_area(self):
        # calculate area of the rectangle
        area = self.width * self.height
        return area

    def get_perimeter(self):
        # calculate the perimeter of the rectangle
        perimeter = 2 * self.width + 2 * self.height 
        return perimeter

    def get_diagonal(self):
        # calculates diagonal of rectangle
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        # builds a shape w/ *s based on width/height
        # first, determine if the shape is too big
        if (self.width or self.height) > 50:
            return "Too big for picture."
        # if it's not too big, build shape
        shape = ""
        for i in range (0, self.height):
            shape = shape + "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, shape):
        # calculate how many of a given shape fits in this shape
        is_width = shape.width # stands for inside shape width
        is_height = shape.height
        if  (((is_height / self.height) < 1) or ((is_width / self.width))) < 1:
            return 0
        x = self.width / is_width
        y = self.height / is_height
        shapes_inside = x * y
        return int(shapes_inside)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, length):
        # square has width and height set to work w/ the rectangle classes, but only takes one argument
        self.width = length
        self.height = length
        self.length = length

    def set_side(self, length):
        # set all sides of square
        self.width = length
        self.height = length
        self.length = length

    def set_width(self, length):
        # since we are dealing w/ equal width and height, this does the same thing as set_side
        self.width = length
        self.height = length
        self.length = length

    def set_height(self, length):
        # since we are dealing w/ equal width and height, this does the same thing as set_side
        self.width = length
        self.height = length
        self.length = length
            
    def __str__(self):
        return f"Square(side={self.length})"

# below are the examples provided for the assignment
# i have commented them all out b/c they are not needed for the test but were used to help me write the class
# basic tests are below:
'''
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture()) # possibly fixed now

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq) # fixed
print(sq.get_picture()) # possibly fixed now

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq)) # another error here
'''

# should return:
'''
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8'''