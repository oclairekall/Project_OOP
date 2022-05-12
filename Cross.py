import Snowboarding

class Cross(Snowboarding):
  mgold = "AUT Alessandro Haemmerle"
  msilver = "CAN Eliot Grondin"
  mbronze = "ITA Omar Visintin"
  wgold = "USA Lindsey Jacobellis"
  wsilver = "FRA Chloe Treseuch"
  wbronze = "CAN Meryeta Odine"
  def __init__(self, venue:str, scorestyle:str) -> None:
    super().__init__(self, venue, scorestyle)

def __str__(self)->str: