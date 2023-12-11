# using for loop
def even_cubes(input_list: list):
    cube_list = []
    for i in input_list:
        if type(i) is int and i % 2 == 0:
            cube_list.append(i**3)
    return cube_list


# using list comprehension
def even_cubes_list_comprehension(input_list: list):
    cube_list = [i**3 for i in input_list if type(i) is int and i % 2 == 0]
    return cube_list


values = [3, 4, 3, 5, 2, 4, 5, 5, 6, 3, (3, 2, 46, 2)]
print(even_cubes(values))
print(even_cubes_list_comprehension(values))
