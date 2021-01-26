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

    def get_area(self, width, height):
        area = width * height
        return area

    def get_perimeter(self, width, height):
        perimeter = 2 * width + 2 * height # this shouldn't need ()
        return perimeter

    def get_diagonal(self, width, height):
        diagonal = (width ** 2 + height ** 2) ** .5
        return diagonal

    # this method has not yet been tested
    def get_picture(self, width, height):
        if width or height > 50:
            return "Too big for picture."
        # build shape
        shape = ""
        for i in range (0, height):
            if i != 0:
                shape = shape + "\n"
                shape = shape + "*" * width
            else:
                shape = "*" * width
        return shape

    def get_amount_inside(self, shape):
        shape.width = is_width # short for inside shape width
        shape.height = is_height # getting an undefined variable error here, need to correct, or maybe just finish this.

    