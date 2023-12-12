# Task a: Print total number of characters, words, and lines in the file
def count_chars_words_lines(filename):
    with open(filename, 'r') as file:
        text = file.read()
        char_count = len(text)
        word_count = len(text.split())
        line_count = text.count('\n') + 1  # Counting '\n' to calculate lines

    print(f"Total number of characters: {char_count}")
    print(f"Total number of words: {word_count}")
    print(f"Total number of lines: {line_count}")

# Task b: Calculate frequency of each character in the file
def char_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
        freq_dict = {}
        for char in text:
            freq_dict[char] = freq_dict.get(char, 0) + 1

    print("Character frequency:")
    for char, freq in freq_dict.items():
        print(f"'{char}': {freq}")

# Task c: Print words in reverse order
def reverse_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        reversed_words = ' '.join(words[::-1])

    print("Words in reverse order:")
    print(reversed_words)

# Task d: Copy even lines to 'File1' and odd lines to 'File2'
def copy_even_odd_lines(filename):
    with open(filename, 'r') as file:
        even_lines = []
        odd_lines = []
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            if i % 2 == 0:
                even_lines.append(line)
            else:
                odd_lines.append(line)

    with open('File1.txt', 'w') as file1:
        file1.writelines(even_lines)

    with open('File2.txt', 'w') as file2:
        file2.writelines(odd_lines)

# File to perform operations on
file_to_read = 'sample.txt'  # Replace 'sample.txt' with your file name

# Perform the tasks
count_chars_words_lines(file_to_read)
print()
char_frequency(file_to_read)
print()
reverse_words(file_to_read)
copy_even_odd_lines(file_to_read)
