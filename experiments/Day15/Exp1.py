import glob

myfiles = glob.glob('files/*.txt')
# Returns a list with all the files of the specified type on the folder

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())


