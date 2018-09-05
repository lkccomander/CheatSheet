import code

class CCMPcode:
    """description of class"""
        
    name = ""
    category = ""
    pcode = 0

    def __init__(self, name, category, pcode):
          print("This is the constructor method.")
          self.name = name
          self.category = category
          self.pcode = pcode


    def displayCCMPcode(self):
          print("Name : ", self.name,  ", Category: ", self.category ,", Code: ", self.pcode)


