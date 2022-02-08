# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from itertools import product


def get_pins(observed):

    possible_numbers = {
        "1": ["1", "2", "4"],
        "2": ["2", "1", "3", "5"],
        "3": ["3", "2", "6"],
        "4": ["4", "1", "5", "7"],
        "5": ["5", "2", "4", "6", "8"],
        "6": ["6", "5", "3", "9"],
        "7": ["7", "4", "8"],
        "8": ["8", "5", "7", "9", "0"],
        "9": ["9", "8", "6"],
        "0": ["0", "8"],
    }
    possible_pins = []

    possibilities = []
    for i in range(len(observed)):
        possibilities.append([])

    for idx, num in enumerate(str(observed)):
        for i in possible_numbers[num]:
            possibilities[idx].append(i)

    pins = list(product(*possibilities))
    for i in pins:
        pin = ""
        for j in i:
            pin += j
            if len(pin) == len(observed):
                possible_pins.append(pin)

    return possible_pins
