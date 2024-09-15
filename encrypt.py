#Name: Hasin Shadab Rahman                                                                UID:U87513234
# The program uses a dictionary (Encrypt_Code) for character mapping to encrypt a text file.
# encrypt_text(input_text) function encrypts the input text according to the dictionary, preserving spaces and characters not in the dictionary.
# main() is the main function that prompts the user to specify the input and output text file names.
# It reads the input text file, encrypts its content, and writes the encrypted text to the output file.
#E.g. Input file: Bye.txt Output file: Hello.txt
# The program handles the case where the input file is not found with a FileNotFoundError message.
# To use the program:

# Run the script.
# Enter the input text file name.
# Specify the output text file name for the encrypted content.
# The program reads, encrypts, and saves the content to the output file.
Encrypt_Code = {
    'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8',
    'D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5',
    'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2',
    'J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y',
    'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v',
    'P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's',
    'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p',
    'V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm',
    'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j',
    '@': 'I', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g',
    '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd',
    '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a',
    ':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<',
    "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=',
    '{': '[', '[': '{', '}': ']', ']': '}'
}

def encrypt_text(input_text):
    encrypted_text = ''
    for char in input_text:
        if char.isspace():
            encrypted_text += char  # Keep spaces as they are
        elif char in Encrypt_Code:
            encrypted_text += Encrypt_Code[char]
        else:
            encrypted_text += char  # Keep any character not in the dictionary as-is
    return encrypted_text

def main():
    input_file_name = input("Enter the name of the input text file: ")
    output_file_name = input("Enter the name of the output text file: ")

    try:
        with open(input_file_name, 'r') as input_file:
            text = input_file.read()

        encrypted_text = encrypt_text(text)

        with open(output_file_name, 'w') as output_file:
            output_file.write(encrypted_text)

        print("Encryption complete. Output saved to", output_file_name)
    except FileNotFoundError:
        print("File not found. Please check the file name.")

if __name__ == "__main__":
    main()
