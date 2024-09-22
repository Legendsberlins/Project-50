import emoji

text = input("Input: ")
convert = emoji.emojize(text, language="alias")
print(f"Output: {convert}")
