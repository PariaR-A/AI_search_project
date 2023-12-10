import re

def extract_digit_and_word(string):
    """
    our matrix value might be combination of letters and digits so we might need this to parse it
    """
    match = re.match(r"(\d+)(\w+)", string)

    if match:
        digit_part = match.group(1)
        word_part = match.group(2)
        return digit_part, word_part
    else:
        return None, None

class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def print_colorful_text(text, color):
    colored_text = f"{color}{text}{Color.RESET}"
    return colored_text
