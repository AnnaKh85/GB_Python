path_to_file = 'log.csv'

def whitespase():
    with open(path_to_file) as file:
        for num_line, line in enumerate(file):
            num_line = 1 + num_line
            with open('separator_whitespace.csv','a') as file:
                if num_line % 2 == 0:
                    file.write(line)
                elif num_line > 1:
                    file.write('\n')

def comma():
    with open(path_to_file) as file:
        for num_line, line in enumerate(file):
            num_line = 1 + num_line
            with open('separator_comma.csv','a') as file:
                if num_line %2 == 0 and num_line!=2:
                    a = line.replace('\n',',').replace('|','').replace('         ',' ')
                    file.write(a)