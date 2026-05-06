def main():
    # get user input and remove surrounding whitespace
    user_input = input("Enter your message: ").strip()

    # logical check
    if user_input:
        print(user_input.lower())
    else:
        # handling empty input case
        print("input is empty!")


main()

