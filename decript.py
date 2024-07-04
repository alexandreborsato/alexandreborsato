# Python program to encript a plain text in a very simple way

# Functions created below

def get_user_input():
    user_input = input("Please enter a plain text to decript: ")
    return user_input

def char_array_to_int_array(char_array):
    int_array = [ord(char) for char in char_array]
    return int_array

def add_constant_to_array(arr, constant):
    return [num - constant for num in arr]

def int_array_to_char_array(int_array):
    cript_char_array = [chr(num) for num in int_array]
    return cript_char_array

def char_array_to_string(echar_array):
    return ''.join(echar_array)

def generate_output_file(output_filename, content):
    with open(output_filename, 'w') as file:
        file.write(content)

# Getting Initial Text and converting to array, and so, converting to ascii code;
# adding 3 to ascii code to codify so converting the original text into a coded text:
user_string = get_user_input()
string_length = len(user_string)
user_char_array = list(user_string)
user_int_array = char_array_to_int_array(user_char_array)
result_array = add_constant_to_array(user_int_array, 3)
encript_char_array = int_array_to_char_array(result_array)
encripted_user_string = char_array_to_string(encript_char_array)

output_filename = "o-file.txt"
output_filename = input("Please enter a file name as output for the decripted text: ")
generate_output_file(output_filename, encripted_user_string)

# printing everything

print("User String:", user_string)
print("Input Char Array:", user_char_array)
print("Array Length:", string_length)
print("Integer Array:", user_int_array)
print("Result Array (with constant added):", result_array)
print("Result Encripted Array:", encript_char_array)
print("Encripted String:", encripted_user_string)
print(f"File '{output_filename}' created with the given content.")
