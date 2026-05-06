def slow_down(text):
    # split text into a list of words.
    words = text.strip().split()
    # rejoin words using "..." as a separator
    return "...".join(words)


def main():
    msg = input()
    print(slow_down(msg))


main()
