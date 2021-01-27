class Rectangle:

    # rectangle has two parameters, width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        # unsure if this needs to return anything at this time

    def set_height(self, height):
        self.height = height
        # also unsure if this needs to return anything

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height # this shouldn't need (), I hope
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    # this method has not yet been tested
    def get_picture(self):
        if self.width or self.height > 50:
            return "Too big for picture."
        # build shape
        shape = ""
        for i in range (0, self.height):
            if i != 0:
                shape = shape + "\n"
                shape = shape + "*" * self.width
            else:
                shape = "*" * self.width
        return shape

    def get_amount_inside(self, shape):
        is_width = shape.width # stands for inside shape width
        is_height = shape.height
        if ((is_height / self.height) < 1) or ((is_width / self.width) < 1):
            return 0
        x = is_width / self.width
        y = is_height / self.height
        shapes_inside = x * y # this probably won't work but hey, it's an early draft
        return shapes_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length
        self.length = length

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, length):
        self.width = length
        # unsure if this needs to return anything at this time

    def set_height(self, length):
        self.height = length
        # also unsure if this needs to return anything    
            
    def __str__(self):
        return f"Square(side={self.length})"

# basic tests are below:
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture()) # needs fixed

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq) # error here
print(sq.get_picture()) # another error here

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq)) # another error here

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