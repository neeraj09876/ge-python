n = int(input("Enter the number of stars in Pyramid(odd) : "))

spaces = " " * int(n/2)
counter = 1
# Upper pyramid
for i in range(1, n+1, 2):
    print(spaces + ("*" * i))
    spaces = " " * (int(n/2) - counter)
    counter += 1

# Reverse pyramid
counter = 1
for i in range(n-2, 0, -2):
    spaces = " " * counter
    print(spaces + ("*" * i))
    counter += 1
    
