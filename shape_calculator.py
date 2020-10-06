class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
  def set_width(self,width):
    self.width=width
  def set_height(self,height):
    self.height=height
  def get_area(self):
    return self.width*self.height
  def get_perimeter(self):
    return 2*(self.width+self.height)
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_picture(self):
    if(self.width>50 or self.height>50):
      return "Too big for picture."
    p=""
    for w in range(0,self.height):
      p+="*"*self.width+"\n"
    return p
  def get_amount_inside(self,rec):
    return int(self.width/rec.width)*int(self.height/rec.height)
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self,side):
    super(Square,self).__init__(side,side)
  def set_side(self,side):
    self.width=side
    self.height=side
  def set_width(self,side):
    self.set_side(side)
  def set_height(self,side):
    self.set_side(side)
  def __str__(self):
    return f"Square(side={self.width})"