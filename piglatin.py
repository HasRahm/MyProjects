#Name: Hasin Shadab Rahman                                                       UID: U87513234
# The program converts text from an input file(Bye.txt) to Pig Latin and saves the result in an output file(Good.txt).
# pig_latin_word(word) converts a single word to Pig Latin, handling capitalization and preserving punctuation.
# convert_to_pig_latin(input_text ) processes the entire input text, splitting it into words and applying Pig Latin conversion.
# The main() function guides the user to input the file names, reads the input text, and writes the Pig Latin output.
# The program ensures punctuation and capitalization are preserved in the output.
# It handles situations where the input file is not found.
# To use the program:

# Run the script and provide the input text file name.
# Enter the output file name to save the Pig Latin translation.
# The program will process the text, convert it to Pig Latin, and save it in the output file.
def pig_latin_word(word):
    if word.isalpha():
        if word[0].isupper():
            return word[1:].lower() + word[0].lower() + 'ay'
        else:
            return word[1:] + word[0] + 'ay'
    else:
        punc = ''
        while word and not word[-1].isalnum():
            punc = word[-1] + punc
            word = word[:-1]
        return word + punc

def convert_to_pig_latin(input_text):
    words = input_text.split()
    pig_latin_words = [pig_latin_word(word) for word in words]
    return ''.join(pig_latin_words)

def main():
    input_file_name = input("Enter the name of the input text file: ")
    output_file_name = input("Enter the name of the output text file: ")

    try:
        with open(input_file_name, 'r') as input_file:
            text = input_file.read()

        pig_latin_text = convert_to_pig_latin(text)

        with open(output_file_name, 'w') as output_file:
            output_file.write(pig_latin_text)

        print("Conversion to Pig Latin complete. Output saved to", output_file_name)
    except FileNotFoundError:
        print("File not found. Please check the file name.")

if __name__ == "__main__":
    main()

