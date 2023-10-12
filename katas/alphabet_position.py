def alphabet_position(text):
    new_string = [str(ord(l.lower()) - 96) for l in text if l.isalpha()]
    return ' '.join(new_string)

print(alphabet_position("The sunset"))