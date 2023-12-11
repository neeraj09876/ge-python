characterInput = input("Enter a Character : ")
isInputLetter = False
isInputDigit = False

if characterInput.isalpha():
    isInputLetter = True
    print(characterInput + " is a Letter.")
elif characterInput.isnumeric():
    isInputDigit = True
    print(characterInput + " is a Numeric Digit.")
else:
    print(characterInput + " is a Special Character.")

if isInputLetter:
    if characterInput.isupper():
        print("Entered character is in Upper Case")
    else:
        print("Entered character is in Lower Case")

digitToNameMapping = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                      9: "Nine"}
if isInputDigit:
    print(characterInput + " in words is " + digitToNameMapping[int(characterInput)])
