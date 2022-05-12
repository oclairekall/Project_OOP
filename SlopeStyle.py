import AlpineSkiing

class Slalom(AlpineSkiing):
  mgold = "FRA Clement Noel 1:44.09"
    msilver = "AUT Johannes Strolz 1:44.70"
    mbronze = "NOR Sebastian Foss-Solevaag 1:44.79"
    wgold = "SVK Petra Vlhova 1:44.98"
    wsilver = "AUT Katharina Liensberger 1:45.06"
    wbronze = "SUI Wendy Holdener 1:45.10"
  def __init__(self, venue:str, scorestyle:str) -> None:
    super().__init__(self, venue, scorestyle)
   

#maybe getters here
def __str__(self)->str:
    