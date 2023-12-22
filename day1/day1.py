
input_file = "input.txt"

def read_input(input_file):    
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found")
             
def word_to_digit(word):
    word_to_digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return ''.join(word_to_digit_map.get(char, char) for char in word)

def extract_values(lines):
    total_sum = 0

    for line in lines:
        concatenated_number = ''.join(char for char in line if char.isdigit())
        if concatenated_number:
            total_sum += int(concatenated_number[0] + concatenated_number[-1])

    return total_sum

print(word_to_digit("eightwothree"))


# lines = read_input(input_file)
# sum = extract_values(lines)

# print("Sum: ", sum)