def is_equal(counter_one):
    counter_two = 0
    limit = counter_one + len(string_two)
    for i in range(counter_one, limit):
        if string_one[i] != string_two[counter_two]:
            return False
        counter_two += 1
    return True


def is_present():
    len_first = len(string_one)
    len_second = len(string_two)
    result = []
    counter_one = 0
    while counter_one < len_first:
        if is_equal(counter_one):
            for i in range(counter_one, counter_one + len_second):
                result.append(i)
        counter_one += 1
    if len(result) == 0:
        return -1
    return result


string_one = input("Enter first string: ")
string_two = input("Enter second string: ")
print(is_present())
