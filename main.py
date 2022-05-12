"""
COMP-305 Team Fortran Final Project
Professor: Anuzen
Names: Frank Veldhuizen, Olivia Kallmeyer, Brayan Mendoza, Chris Redd
Purpose: Create terminal based operational version of our Winter Olympic results 
application
"""
import Slalom 
def createOutput(sport, event)->None:

  #handles the special case for icehockey having no events
  if sport == "B" and event == " ":
    obj = IceHockey()

  #handles the case of an event under alpine skiing
  if sport == "A":
    if event == "A":
      obj = Slalom()
    elif event == "B":
      obj = Downhill()
    elif event == "C":
      obj = SuperG()
    elif event == "D":
      obj = GSlalom()

  #handles the case of an event under snowboarding
  if sport == "C":
    if event == "A":
      obj = ParallelGS()
    elif event == "B":
      obj = BigAir()
    elif event == "C":
      obj = Cross()
    elif event == "D":
      obj = HalfPipe()
    elif event == "E":
      obj = SlopeStyle()
      
  print(obj)

  
def main()->None:
  print("Select desired sport by inputing letter a A,B, or C:")
  print("Alpine Skiing -> (A)")
  print("Ice Hockey -> (B)")
  print("Snowboarding -> (C)")
  sport = input().upper()

  if sport == "A":
    print("Select desired alpine skiing event by inputing a letter A-D:")
    print("Slalom -> (A)")
    print("Downhill -> (B)")
    print("Super-G -> (C)")
    print("Giant Slalom -> (D)")
    event = input().upper()
  
  elif sport == "B":
    event = " "

  elif sport =="C":
    print("Select desired snowboarding event by inputing letter A-E:")
    print("Parallel Giant Slalom -> (A)")
    print("Big Air -> (B)")
    print("Cross -> (C)")
    print("Halfpipe -> (D)")
    print("Slope Style -> (E)")
    event = input().upper()
  else:
    print("********ERROR, incorrect input********")

  #creates an object and prints out details 
  createOutput(sport, event)
    
   
main()
#if __name__ == "__main__":
  ##calls main method
  #main()