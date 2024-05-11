filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for item in filenames:
    file = open(f'files\{item}', 'w')
    file.write('Hello')
