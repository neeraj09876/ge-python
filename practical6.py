strOne = input("Enter the first String : ")
strTwo = input("Enter the second String : ")

n = int(input("Length of the string to be swapped : "))

if n <= min(len(strOne), len(strTwo)):
    temp = strOne[0: n]
    strOne = strOne.replace(temp, strTwo[0: n])
    strTwo = strTwo.replace(strTwo[0: n], temp)
    print("First String :", strOne)
    print("Second String :", strTwo)
else:
    print("Wrong Input!!")
