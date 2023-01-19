class Boat:

    def __init__(self, length, hit_point, is_alive,) :
        self.length = length
        self.hit_point = hit_point
        self.is_alive = is_alive
        self.has_played = False


    def is_alive(self):
        if(self.length - self.hit_point <= 0):
            return False
        else:
             return True
    
    def take_hit(self):
        hit_point = hit_point - 1

    def play_boat(self):
        has_played = True