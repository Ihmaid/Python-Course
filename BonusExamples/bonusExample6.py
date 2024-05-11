contents = ['All carrots are to be sliced longitudinally.',
            'The carrots were reportedly sliced.',
            'The slicing process was well presented.']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):     # Do as the enumerate function, but fetch the correspondent
    file = open(f'../files/{filename}', 'w')           # item of two lists
    file.write(content)
