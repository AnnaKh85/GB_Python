# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'На форму настроекабв отчета добавить реквиабвзит Валюта \
            (по умолчанию, заполнеабвно AVG Xrate EUR). Пользователь может выбирабвать любую валюту. \
            Для расчабветов необходимо отбирать куабврс на дату Окончания настроек отчета.'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)
