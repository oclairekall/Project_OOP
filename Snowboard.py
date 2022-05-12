# snowboarding class
class Snowboarding(object):
  

  #def __init__(self, venue:str, scorestyle:str) -> None:
    #self.venue = venue
    #self.scorestyle = scorestyle
  
  def __str__(self)->str:
    if self.venue == None and self.scorestyle == None:
      self.venue = "N/A"
      self.scorestyle = "N/A"
    return f" ================================== \n Snowboarding: \n details... \n Venue: {self.venue} \n Scoring Style: {self.scorestyle}" 
