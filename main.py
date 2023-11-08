from functions import *

text_file = "test.txt"

with open(text_file) as f:
    content = f.readlines()

text = "".join(content)

new = remove_duplicate(text)
# print(new)

with open("cleaned_test_file", "w") as f:
    for line in new:
        f.write(line)
        # f.write("")
