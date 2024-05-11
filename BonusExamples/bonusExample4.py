filenames = ['1.Raw Data.txt', '2.Reports.text', '3.Presentations.txt']

for file in filenames:
    file = file.replace('.', '-', 1)
    print(file)

# If you want a immutable list, is necessary to use a tuple -> filenames = (xxxx) with brackets
