from functions import *

text_file = "This this is Is a practice test test file."

# with open(text_file) as f:
#     content = f.readlines()

# text = " ".join(content)

new = remove_duplicate(text_file)
print(new)

# with open("document_name_here", "w") as f:
#     for line in new:
#         f.write(line)
#         f.write("")
