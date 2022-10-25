import random
from .classes.equation import Equation

def create_times_table(max: int) -> list[Equation]:
    table = []
    for i in range(1, max + 1):
        for j in range(1, max + 1):
            table.append(Equation(i, j))
    return table

def get_equation_list(times_table: list[Equation], count: int):
    i = 0
    equation_list = []
    times_table_copy = times_table[:]
    while i < count:
        if (len(times_table_copy) == 0):
            times_table_copy = times_table[:]
        index = random.randint(0, len(times_table_copy) - 1)
        equation_list.append(times_table_copy[index])
        del times_table_copy[index]
        i += 1
    return equation_list