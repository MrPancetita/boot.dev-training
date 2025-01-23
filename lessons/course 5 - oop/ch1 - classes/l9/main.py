# https://www.boot.dev/lessons/28072480-92b7-40e7-9a82-09f0a9b0241d

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
