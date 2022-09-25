path_to_file = 'log.csv'

def search():
    find = input('Please enter the search data: ')
    with open(path_to_file) as file:
        for num_line, line in enumerate(file):
            num_line = 1 + num_line
            with open('search.csv', 'a') as file:
                if num_line % 2 == 0 and find in line:
                    file.write(line)
