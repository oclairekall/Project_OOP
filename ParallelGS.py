import Snowboarding

# Parallel Giant Slalom Class
class ParallelGS(Snowboarding):
  def __init__(self, venue:str, scorestyle:str) -> None:
    super().__init__(self, venue, scorestyle)
    mgold = "AUT Benjamin Karl"
    msilver = "SLO Tim Mastnak"
    mbronze = "ROC Vic Wild"
    wgold = "CZE Ester Ledecka"
    wsilver = "AUT Daniela Ubling"
    wbronze = "SLO Gloria Kotnik"

#maybe need getters here? idk
  def __str__(self)->str:
    