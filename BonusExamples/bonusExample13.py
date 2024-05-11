# Here we decoupled the function of bonus12, that is, we reduce the bigger function on 2 smaller functions.
# Functions need to do one service and do it well
def parse(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet': feet, 'inches':  inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
        # Do not complexify the output of the function. This is decoupling
    return meters


feet_inches_in = input('Enter feet and inches: ')
parsed = parse(feet_inches_in)
result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet  and {parsed['inches']} is equal to {result}")

if result < 1:
    print('Kid is too small.')
else:
    print("Kid can use the slide.")
