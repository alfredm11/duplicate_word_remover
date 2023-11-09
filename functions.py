import re
from collections import OrderedDict


def remove_duplicate(text):

    # Remove duplicated word.
    # Example: many many, for for, has has, etc.

    pattern = re.compile(r'(([a-zA-Z]+)\s)\1', flags=re.IGNORECASE)
    matches = pattern.findall(text)

    sub_words = pattern.sub(r'\1', text)
    return sub_words


def remove_duplicate_comma(text):

    # Removes duplicated words with comma.
    # Example: (in, in, in), (very, very, very)

    pattern = re.compile(r'(([a-zA-Z]+)\,)\s\1{,}', flags=re.IGNORECASE)
    matches = pattern.findall(text)

    sub_words = pattern.sub(r'\1', text)
    return sub_words


def setter(text):

    # This will put values in a set in order
    # Then it will return a string

    my_list = text.split()
    new_list = OrderedDict.fromkeys(my_list)
    new_string = " ".join(new_list)
    return new_string
