import json


def convert_coordinates(coords):
    converted = []
    for coord in coords:
        x = ord(coord[0]) - ord('a')
        y = ord(coord[1]) - ord('a')
        converted.append([x, y])
    return converted
