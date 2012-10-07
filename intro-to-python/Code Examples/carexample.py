class Car:
  def init(self):
    self.speed = 0
    self.occupants = 0
    self.direction = 0
  
  def steer ( self , dirchange ):
    self.direction = (self.direction + dirchange) % 360

  # TODO: Add accelerate( speed_difference ), get_in(), get_out()

  