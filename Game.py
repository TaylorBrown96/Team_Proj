
import Player
from rooms import Room

#Create the prompt inside the game loop and provide the commands that will 
# be used from the function of gameloop.

class Game: 
    """
    The main protocol for creating the game loop and other responisbilities
    for which the game class will handle. This way this will handle the main
    functions in which will be created and stored inside. This allows for a 
    smooth set up
    """
    
    def __init__(self):
        """Creates the empty rooms and files for set up"""
        #self.player = player.Player
        self.rooms = {} #The empty dictionary to contain the rooms to be appended too
        #Player object is held in the room (loc)
        self.player = Player
        
        self.isplaying = True
        self.isVerbose = True #This is the way to change verb commands
        
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def setup(self):
        """Setup() creates the rooms for playing"""
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
                                      "north": "bar",
                                      "east": "Lab",
                                      "west": "Gas Station"})
 
                                  
        wilderness = Room ("Wilderness", """
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """, {"north": "Town Center",
                                      "east": "Gas Station",
                                      "west": "Lab"})
                        
        lab = Room ("Lab", """
               High rusty fence with a sign reading
               Restricted Area come at your own risk.
               Some of the fencing was bent over and you could
               easily walk over. Back towards the West is the open wilderness.
               """, {"west": "Town Center",
                     "east": "Wilderness"})
                    
        gasstation = Room("Gas Station", """
                         You arrpoach Jaun's Quick n Fill,
                         A rather small gas station with four pumps.
                         They appear to be old timely compared to what you are used too,
                         from here to the East is the open wilderness, and to the West
                         is the Town Center.
                         """, {"west": "Wilderness",
                               "east": "Town Center"})
                    
            
    
                                
                                
                                
        self.rooms = {bar.name: bar, 
                townCenter.name:  townCenter,
                wilderness.name:  wilderness,
                lab.name: lab,
                gasstation.name: gasstation}
        
        self.here = bar #Starting room and where we will Meet UN Dolphins
        self.here.describe #This is the describe function that will give
        
        
    def loop(self):
            """ loop(): the main game loop.
            Continues until the user quits. """
            self.isPlaying = True
            while self.isPlaying:
                self.playerAction()
            print("The Game is Over, Thank you for Playing")
            
    def end(self):
        pass
    
    def playerAction(self):
        """Asks for the user input and validation"""
        command = input(">")
        command = command.lower()
        words = command.split() # spliting the white space.
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("Quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        else: # first word is verb
            print("I don't know how to", words[0])
            
    
    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: nothing
        Side effects are the player is able to move through the room
        """
        # Can we go in the chosen direction from here?
        print(direction)
        print(self.here.exits)
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            # newRoomName = self.here.exits[direction]
            exitList = self.here.exits.keys() #Gives the directions for the exits.
            for exits in exitList:
                text = direction
                text += ": " + self.here.exits[exits] #Gives the format of bar: smokey bar
                text += "\n" 
            
            print(text)
            newRoomName = self.here.exits[direction]
            print(self.rooms)
            newRoom     = self.rooms[newRoomName]
            
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    
    
    def commandGet(self, item):
        """ remove items from the room so that way it can actaully
            be added to the player inventory.
        """
        print("You try to get the", item)

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()