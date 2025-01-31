class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        # Remember that in range finishes at the last number - 1
        if ((self.pos_x in range(x_1, x_2 + 1)) and (self.pos_y in range(y_1, y_2 + 1))):
            return True


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        fire_area = (x - self.__fire_range, y - self.__fire_range, x + self.__fire_range, y + self.__fire_range)
        hit_units = []
        for unit in units:
            if unit.in_area(*fire_area):
                hit_units.append(unit)
        return hit_units
