def main():
    word = input("")
    final = convert(word)
    print(final)

def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂").replace(":(", "😐")
    return emoticon

main()
