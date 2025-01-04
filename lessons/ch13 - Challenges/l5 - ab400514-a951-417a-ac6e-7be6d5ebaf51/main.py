# https://www.boot.dev/lessons/ab400514-a951-417a-ac6e-7be6d5ebaf51

def area_sum(rectangles):
    areas = []
    for rectangle in rectangles:
        areas.append(rectangle["height"] * rectangle["width"])
    return sum(areas)
