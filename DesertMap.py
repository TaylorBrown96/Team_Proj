class Room: 
    """Rooms are used to maked link lists. They contain a value and a optionally,
        a "pointer" to the next Room."""
        
    def __init__(self, room, desc):
        self.room = room
        self.desc = desc
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    # def __init__(self, value):
    #     self.value = value
    #     self.next = None
    #     self.prev = None





class desertMap:
        
    def __init__(self):
        pass
        
def setup(self):
        
    # def goto(self, direction):
    #     self.direction    
    #     if next_room := self.current_room.goto(direction):
    #             self.current_room = next_room
    #             return next_room

    
    # Create the rooms

        bar = Room("""
               A large open smokey bar, with several round tables
               and stools. The smell of booze in the air, mixed
               with the scent of cigerette smoke. It was hard to see
               through the crowd of people but to the South,
               the main enterance and exit leads to the hot arid
               Desert Outside.
               """)
    
        lab = Room("""
               High rusty fence with a sign reading
               Restricted Area come at your own risk.
               Some of the fencing was bent over and you could
               easily walk over. Back towards the West is the open wilderness.
               """)
    
        gastation = Room("""
                         You arrpoach Jaun's Quick n Fill,
                         A rather small gas station with four pumps.
                         They appear to be old timely compared to what you are used too,
                         from here to the East is the open wilderness, and to the West
                         is the Town Center.
                         """)
    
        wilderness = Room("""
                      As you leave the town square, you find yourself
                      near the canyons, there was a dusty road well traveled.
                      To the East the mirage from the center appears much clear.
                      From your first thoughts it was indeed appears to be a lab,
                      a large rusted fence surrounding it. To the North is where you came,
                      the center of the town. To the West you can make out a sign for the 
                      gas station, it says Jaun's Quick n Fill.
                      """)
    
        towncenter = Room("""
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """)
    
    
        # #Linking the Rooms
        # bar.north = lab
        # lab.east = gastation
        # gastation.south = wilderness
        # wilderness.west = towncenter
        
        # #Linking the Rooms via back and forth
        # towncenter.east = wilderness
        # wilderness.north = gastation
        # gastation.west = lab
        # lab.south = bar
        
        
        #append to the list of rooms
        self.rooms = []
        
   

desert = desertMap