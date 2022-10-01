def DrawMenu(inputMenu):
    menu = inputMenu
    lenght = len(menu)
    print("-----------------------------------------------")
    for i in range(lenght):
        print(f"{i+1}. {menu[i]}")
    print("-----------------------------------------------")
    menuItem=input("Choose the option: ")
    return [menuItem, inputMenu[int(menuItem)-1]]
