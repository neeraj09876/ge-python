strInput = input("Enter the String : ")
calculateFrequencyCharacter = input("Enter the character whose frequency is to be Calculated : ")

# Frequency of each character in String
print("Frequency of " + calculateFrequencyCharacter + " Each Char present in the input String : " + str(strInput.count(calculateFrequencyCharacter)))


# Replace each occurrence of character with new one
replaceCharacter = input("Enter the character to be replaced in the string : ")
newCharacter = input("Enter the new Character : ")
strInputCopy = strInput
strInputCopy = strInputCopy.replace(replaceCharacter, newCharacter)
print(strInputCopy)
