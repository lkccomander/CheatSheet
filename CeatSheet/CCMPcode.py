import code

class CCMPcode:
    """description of class """
        
    name = ""
    category = ""
    pcode = 0

    def __init__(self, name, category, pcode1):
          print("This is the constructor method.")
          self.name = name
          self.category = category
          self.pcode = pcode1


    def displayCCMPcode(self):
          print("Name : ", self.name,  ", Category: ", self.category ,", Code: ", self.pcode)

    def displayCCMPcode1(self):
          print("Name : ", self.name,  ", Category: ", self.category ,", Code: ", self.pcode)

    def displayCCMPcode3(self):
          print("Name : ", self.name,  ", Category: ", self.category ,", Code: ", self.pcode)


