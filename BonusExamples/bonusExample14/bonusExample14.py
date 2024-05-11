# Here we decoupled the function of bonus12, that is, we reduce the bigger function on 2 smaller functions.
# Functions need to do one service and do it well
import functions14

feet_inches_in = input('Enter feet and inches: ')
parsed = functions14.parse(feet_inches_in)
result = functions14.convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet  and {parsed['inches']} is equal to {result}")

if result < 1:
    print('Kid is too small.')
else:
    print("Kid can use the slide.")
