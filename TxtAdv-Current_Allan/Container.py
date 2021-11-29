#Container class
#moving object from container to container

class Container:
    """ This class only handles collections of Items"""
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
         self.contents[item.name] = item
    def remove(self, item):
        #print("@@@ removing", item, "from", self)# debug code
        """Function glitch ITEM DUPE
        ### Contains code is BUGGED and Broke everything
        # if self.contains(item):
        """
        if self.contents[item.name]:#Works better than the
            del self.contents[item.name]#contains function
            #print(self.contents)# debug code
        
    #Broken code
    def moveItemTo(self, item, destination):
        #t TODO: confirm destination is a CONTAINER!
        #print("@@ moving", item, "from", self, "to", destination)#debug code
        destination.add(item)
        self.remove(item)
        
    def listContents(self):
        text = ""
        for key in self.contents:
            text += key
            text += " : " 
            text += self.contents[key].description
            text += "\n"
        return text
    
    """THE SOURCE OF BREAK-AGE"""
    # def (self, itemName):
    #     """quick way to check if item is present. """
    #     # keys() gives us a list of names of items present
    #     itemNameList = list(self.contents.keys())
    #     #print("Content of :",itemNameList,"object", self)
    #     if itemName in itemNameList:
    #         return True
    #     return False