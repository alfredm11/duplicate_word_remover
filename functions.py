import re


def remove_duplicate(text):

    pattern = re.compile(r"\b([a-zA-Z]+)\s?\1\b", flags=re.IGNORECASE)
    matches = pattern.finditer(text)

    sub_words = pattern.sub(r'\1', text)
    return remove_duplicate_comma(remove_duplicate_apostrophe(sub_words))


def remove_duplicate_apostrophe(text):

    pattern = re.compile(r'\b([a-zA-Z]+\'\w)\s?\1\b', flags=re.IGNORECASE)
    matches = pattern.finditer(text)

    sub_words = pattern.sub(r'\1', text)
    return sub_words


def remove_duplicate_comma(text):

    pattern = re.compile(r'(\w+\,)\s\1\s(\w+)', flags=re.IGNORECASE)
    matches = pattern.finditer(text)

    sub_words = pattern.sub(r'\2', text)
    return sub_words
