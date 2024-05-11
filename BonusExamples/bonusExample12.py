feet_inches_in = input('Enter feet and inches: ')


def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
        # Do not complexify the output of the function. This is decoupling
    return meters


result = convert(feet_inches_in)

if result < 1:
    print('Kid is too small.')
else:
    print("Kid can use the slide.")
