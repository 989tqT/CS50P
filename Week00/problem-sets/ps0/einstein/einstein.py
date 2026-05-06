def main():
    # define speed of light (meters per second)
    LIGHT_SPEED = 300_000_000

    try:
        # convert input to integer
        mass = int(input("Mass (kg:) "))
        # apply E = mc^2 using the exponentiation operator (**)
        energy = mass*(LIGHT_SPEED**2)
        print(f"Energy:{energy:,} Joules")

    except ValueError:
        # handle cases where input is not a valid number
        print("please enter mass")


main()
