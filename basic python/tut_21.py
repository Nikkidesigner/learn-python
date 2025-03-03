import sys
script, filename, input_encoding, error = sys.argv

def main(languages, encoding, error):
    line = languages.readline()

    if line:
        print_line(line, encoding, error)
        return main(languages, encoding, error)
    
def print_line(line, encoding, error):
    next_lang = line.strip()
    encoded_string = next_lang.encode(encoding, errors=error)
    decoded_string = encoded_string.decode(encoding, errors=error)

    print(f"The string {next_lang} was encoded to {encoded_string} and decoded back to {decoded_string}")

languages = open(filename , encoding="utf-8")
main(languages , input_encoding , error)

    