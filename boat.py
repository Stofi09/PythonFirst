class Boat:
# Question: is there a static like thing in py? I need an auto increment var., how to make a variable immutable
    def __init__(self, length, id) :
        self.length = length
        self.id = id
        self.hit_point = 0
        self.is_alive = False
        self.has_played = False


    def check_if_alive(self):
        
        if(self.length - self.hit_point <= 0):
            return False
        else:
             return True
    
    def take_hit(self):
        hit_point = hit_point - 1

    def play_boat(self):
        has_played = True
        is_alive = True

boat = Boat(5,1)
print(boat.check_if_alive())