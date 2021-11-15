#Container class
#moving object from container to container

class Container:
    """ This class only handles collections of Items"""
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
        self.contents[item.name] = item
    def remove(self, item):
        if self.contains(item):
            # self.contents.remove(item)
            # remove the item from the dictionary
            del self.contents[item.name]
            print(self.contents)
    def moveItemTo(self, item, destination):
        #t TODO: confirm destination is a CONTAINER!
        print("moveItemTo: ", item.name, "from", self, "to", destination)
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
        
    """Function glitch ITEM DUPE"""
    def contains(self, itemName):
        """quick way to check if item is present. """
        # keys() gives us a list of names of items present
        itemNameList = list(self.contents.keys())
        #print("Content of :",itemNameList,"object", self)
        if itemName in itemNameList:
            return True
        return False
    
def main():
    """ test code"""    

if __name__ == "__main__":
    main()