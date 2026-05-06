def convert(text):
    # use a dictionary to store emoji mappings.
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }

    # replace occurrences
    for pattern, icon in emojis.items():
        text = text.replace(pattern, icon)
    return text


def main():
    user_input = input()
    print(convert(user_input))

main()
