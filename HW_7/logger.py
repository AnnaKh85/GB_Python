from tabulate import tabulate

head = ["Surname", "Name", "Phone number", "Discription"]

def add_data(d):
    with open ('log.csv', 'a') as file:
        file.write(tabulate(d, headers=head, tablefmt="grid"))
