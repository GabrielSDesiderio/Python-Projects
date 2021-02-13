class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_height(self,height):
        self.height=height
    def set_width(self,width):
        self.width=width
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width+2*self.height
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        s=''
        for i in range(self.height):
            s+='*'*self.width+'\n'
        return s
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)
    def get_amount_inside(self,other):
        return (self.width//other.width)*(self.height//other.height)
    

class Square(Rectangle):
    def __init__(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.height=side
        self.width=side
    def __str__(self):
        return "Square(side={})".format(self.width)
    def set_height(self,side):
        self.height=side
        self.width=side
    def set_width(self,side):
        self.height=side
        self.width=side