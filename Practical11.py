t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# Print half the values of the tuple in one line and the other half in the next line
half_length = len(t1) // 2
print("Half of the values in one line:")
print(t1[:half_length])
print("\nOther half of the values in the next line:")
print(t1[half_length:])

# Print another tuple whose values are even numbers in the given tuple
even_numbers = tuple(num for num in t1 if num % 2 == 0)
print("\nTuple with even numbers only:", even_numbers)

# Concatenate a tuple (11, 13, 15) with t1
t2 = t1 + (11, 13, 15)
print("\nConcatenated tuple:", t2)

# Return maximum and minimum value from this tuple
max_value = max(t1)
min_value = min(t1)
print("\nMaximum value in the tuple:", max_value)
print("Minimum value in the tuple:", min_value)
