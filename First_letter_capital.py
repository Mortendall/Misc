#! python3
#First_letter_capital.py - Makes first letter capital in list

import pyperclip
text = pyperclip.paste()

lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = lines[i].capitalize()
text = "\n".join(lines)
pyperclip.copy(text)