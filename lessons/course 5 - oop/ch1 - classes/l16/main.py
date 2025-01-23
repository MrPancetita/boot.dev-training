# https://www.boot.dev/lessons/7d643d0f-b009-4ba6-b761-67cea209f5c8

class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        if self.health > 1:
            self.health -= 1
        else:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        else:
            self.num_arrows -= 1
            print (f"{self.name} shoots {target.name}")
            target.get_shot()

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
