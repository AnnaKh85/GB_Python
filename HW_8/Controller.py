import sys
import menu
import DB_operations

def button_click():
    menuList = ['Add info (1)', 'Show DB (2)', 'Exit (3)']
    menuChoice = menu.DrawMenu(menuList)
    match menuChoice[0]:
        case '1':
            DB_operations.AddRecord()
        case '2':
            DB_operations.ShowRecords()
        case '3':
            sys.exit()

