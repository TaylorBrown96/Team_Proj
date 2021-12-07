#Creating the room Class for the testing of movement of the character.

class Room:
    """
    The creation of the room class to make sure that automation can be done
    to secure the code. This is the prototype of the final verison of the
    main room class which will be used for later in a todo.
    """
    
    def __init__(self, name, description, exits):
        """Creates the empty room for initalization purposes"""
        self.name = name
        self.description = description
        self.exits = exits
        self.contents = []
        
    # def __init__(self, name, description, exits):
    #     self.name = name
    #     self.description = description
    #     self.exits = exits
        
    def __str__(self):
        """Creates the rooms and appends them to the list in a human like way"""
        text = self.name + "\n"
        text += self.description + "\n"
        #Appening the exits to the list to be able to be done in one pass
        exitList = self.exits.keys() #Gives the directions for the exits.
        for direction in exitList:
            text += direction
            text += ": " + self.exits[direction] #Gives the format of bar: smokey bar
            text += "\n" 
        
        return text
    
     #   def __repr__(self):  # we're not using this yet
     #   pass
 
    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.


def main():
     bar = Room ("bar", """
               A large open smokey bar, with several round tables
               and stools. The smell of booze in the air, mixed
               with the scent of cigerette smoke. It was hard to see
               through the crowd of people but to the South,
               the main enterance and exit leads to the hot arid
               Desert Outside.
               """, {"south": "Town Center"})
               
     townCenter = Room ("Town Center", """
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """, {"south": "Wilderness",
                                      "north": "Bar",
                                      "east": "Lab",
                                      "west": "Gas  Station"})
    
     wilderness = Room ("Wilderness", """
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """, {"north": "Town Center",
                                      "east": "Gas Station",
                                      "Wwst": "Lab"})
                        
     lab = Room ("Lab", """
               High rusty fence with a sign reading
               Restricted Area come at your own risk.
               Some of the fencing was bent over and you could
               easily walk over. Back towards the West is the open wilderness.
               """, {"west": "Town Center",
                     "east": "Wilderness"})
    
                                
                                
                                
     roomDict = {bar.name: bar, 
                townCenter.name:  townCenter,
                wilderness.name:  wilderness,
                lab.name: lab}