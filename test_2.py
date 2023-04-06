import re

regex = r"\b\w*(\w)\1{2,}\w*\b"

word = "bookkeeperr"
if re.search(r"\b\w*(\w)\1{2,}\w*\b", word):
    print("The word contains 3 or more repetitions.")
else:
    print("The word does not contain 3 or more repetitions.")