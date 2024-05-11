def get_media(numbers_par):
    with open(f'{numbers_par}', 'r') as file:
        numbers_local = file.readlines()
    numbers_local = [float(i) for i in numbers_local]
    media = sum(numbers_local) / len(numbers_local)
    return media


print(get_media('numbers'))
