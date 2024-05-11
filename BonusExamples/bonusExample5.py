waiting_list = ['sen', 'ben', 'john']
waiting_list.sort()  # It is possible to sort in descending order only putting the attribute reverse = True
                        # inside the brackets of the sort function

for index, name in enumerate(waiting_list):
    print(f'{index + 1}.{name.capitalize()}')
