import re
import math


def mull_it_over():
    with open("data/3.txt") as f:
        memory = f.read()

    real_instructions = re.findall(r"mul\((-?\d+),(-?\d+)\)", memory)
    s = 0
    for instruction in real_instructions:
        s += int(instruction[0]) * int(instruction[1])

    print(f"Star 1: {s}")

    dos = [i for i in range(len(memory)) if memory.startswith("do()", i)]
    donts = [i for i in range(len(memory)) if memory.startswith("don't()", i)]

    new_memory = ""
    add = True
    next_stop = donts.pop(0)
    next_start = dos.pop(0)
    for i, c in enumerate(memory):
        if i == next_stop:
            add = False
            if len(donts):
                next_stop = donts.pop(0)
            else:
                next_stop = math.inf
        elif i == next_start:
            add = True
            if len(dos):
                next_start = dos.pop(0)
            else:
                next_start = math.inf
        if add:
            new_memory += c

    do_instructions = re.findall(r"mul\((-?\d+),(-?\d+)\)", new_memory)
    s = 0
    for instruction in do_instructions:
        s += int(instruction[0]) * int(instruction[1])

    print(f"Star 2: {s}")


if __name__ == "__main__":
    mull_it_over()
