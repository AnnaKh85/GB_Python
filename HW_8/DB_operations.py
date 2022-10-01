import Controller
import menu
import pandas as pd

def ShowRecords():
    viewList = ['Show all records', 'Find the record with ID']

    #Read the file
    df = pd.read_excel('school_list.xlsx')

    viewMode = menu.DrawMenu(viewList)[0]

    if viewMode == '1':
        print(df)
        Controller.button_click()
    else:
        recordID = int(input('Enter the record ID: '))

        FindRec = df[df['ID'] == recordID]

        print(FindRec)

        Controller.button_click()

def AddRecord():
    #Add record to the file
    df = pd.read_excel('school_list.xlsx')

    ID = int(input('Enter ID: '))
    LastName = input('Enter the LastName: ')
    FirstName = input('Enter the FirstName: ')
    BirthDate = input('Enter the BirthDate: ')
    Progress = input('Enter the progress of student: ')
    Sex = input('Male or Female: ')

    newRow = {
        'ID': [ID], 'LastName': [LastName], 'FirstName': [FirstName], 'BirthDate': [BirthDate], 'Progress': [Progress],
        'Sex': [Sex]
    }

    df2 = pd.DataFrame(newRow)
    print(df2)

    withNewRow = pd.concat([df, df2], keys=['ID', 'LastName', 'FirstName', 'BirthDate', 'Progress', 'Sex'], ignore_index=True)

    print(withNewRow)

    withNewRow.to_excel('school_list.xlsx')

    Controller.button_click()
