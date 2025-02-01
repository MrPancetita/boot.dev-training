class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type != other.sword_type or self.sword_type == "steel":
            raise ValueError("cannot craft")
        else:
            if self.sword_type == "bronze":
                return Sword("iron")
            elif self.sword_type == "iron":
                return Sword("steel")
