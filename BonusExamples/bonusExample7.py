filenames = ['1.doc', '1.report', '1.presentation']

# The way I did by myself
# i = 0
# for item in filenames:
#     item = item.replace('.', '-') + '.txt'
#     filenames[i] = item
#     i += 1
# print(filenames)

# The right way, list comprehension
filenames = [item.replace('.', '-') + '.txt' for item in filenames]
print(filenames)
