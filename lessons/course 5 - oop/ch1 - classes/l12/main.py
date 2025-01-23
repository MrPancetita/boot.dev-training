# https://www.boot.dev/lessons/896116cd-38a8-4401-a36d-3557a0214a44

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

