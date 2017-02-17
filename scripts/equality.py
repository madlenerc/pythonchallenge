# level 3
with open('../data/equality.txt') as f:
    text = f.read()

    guarded = []

    for i, char in enumerate(text):
        if (char.islower() and text[i - 4].islower() and text[i - 3].isupper() and text[i - 2].isupper() and
                text[i - 1].isupper() and text[i + 1].isupper() and text[i + 2].isupper() and text[i + 3].isupper()
                and text[i + 4].islower()):
            guarded.append(char)

    print(guarded)
