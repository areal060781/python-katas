FIXED_LENGTH = 70

def right_justify(parameter):
    white_fills = FIXED_LENGTH - len(parameter)
    filled_text = (" " * white_fills) + parameter
    return filled_text


