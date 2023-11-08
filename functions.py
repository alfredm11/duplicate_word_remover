import re


def remove_duplicate(text):
    '''
        Remove duplicated word.
        Example: many many, for for, has has, etc.
    '''

    pattern = re.compile(r"\b([a-zA-Z]+)\s?\1\b", flags=re.IGNORECASE)
    matches = pattern.finditer(text)

    sub_words = pattern.sub(r'\1', text)
    return sub_words


def remove_duplicate_apostrophe(text):
    '''
        Remove duplicated contracted word regardless of case.
        Example: It's it's, He's he's, etc.

    '''
    pattern = re.compile(r'\b([a-zA-Z]+\'\w)\s?\1\b', flags=re.IGNORECASE)
    matches = pattern.finditer(text)
    sub_words = pattern.sub(r'\1', text)
    return sub_words


def remove_duplicate_comma(text):
    '''
        Removes duplicated words with comma.
        Example: (in, in, in), (very, very, very)
    '''
    pattern = re.compile(r'(\w+\,)\s\1\s(\w+)', flags=re.IGNORECASE)
    matches = pattern.finditer(text)

    sub_words = pattern.sub(r'\2', text)
    return sub_words
