import sqlite3
import sys
import os
import platform
from prettytable import PrettyTable

conncted_db = sqlite3.connect("langs.db")
cursor = conncted_db.cursor()

clear = lambda: os.system('clear' if platform.system() == 'Linux' or platform.system() == 'MacOS' else 'cls')

def init_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS languages (
        _id INTEGER PRIMARY KEY,
        Name TEXT,
        Extension TEXT,
        IsCompiled BOOLEAN,
        Creator TEXT,
        DateOfBirth YEAR,
        IsHighLevel BOOLEAN,
        SupportedPlatforms TEXT,
        License TEXT,
        OfficialSite TEXT
    );
    ''')

    conncted_db.commit()

    stored_data = [
        ('Python3', 'py', False, "Guido van Rossum", '1991', True, "Crossplatform", "Python Software Foundation License (PSFL)", "https://python.org"),
        ('Java', 'java', True, "James Gosling", '1995', True, "Crossplatform", "GNU GPL", "https://www.oracle.com/java/"),
        ('Я', 'п', False, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "Python Software Foundation License (PSFL)", "https://python.org"),
        ('Слишком', 'р', True, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "Python Software Foundation License (PSFL)", "https://python.org"),
        ('Ленивый', 'о', True, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "OpenSource", "https://python.org"),
        ('Чтобы', 'с', True, "Vladimir fon Mekhtiev I", '2022', True, "Mac", "Python Software Foundation License (PSFL)", "https://python.org"),
        ('Нормально', 'т', False, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "BSD", "https://python.org"),
        ('Заполнить', 'и', True, "Vladimir fon Mekhtiev I", '2022', True, "Linux", "MIT", "https://python.org"),
        ('Эту ', 'т', False, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "Python Software Foundation License (PSFL)", "https://python.org"),
        ('Таблицу', 'е', False, "Vladimir fon Mekhtiev I", '2022', True, "Crossplatform", "Python Software Foundation License (PSFL)", "https://python.org"),
    ]

    cursor.executemany("INSERT INTO languages(Name, Extension, IsCompiled, Creator, DateOfBirth, IsHighLevel, SupportedPlatforms, License, OfficialSite) VALUES (?,?,?,?,?,?,?,?,?);", stored_data)
    conncted_db.commit()

def scroll():
    sql = 'SELECT * FROM languages'
    cursor.execute(sql)
    res = cursor.fetchall()
    clear()
    
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Extension", "IsCompiled", "Creator", "Date of creation", "Is High Level", "Supported Platforms", "License", "Official Site"]
    table.add_rows(res)
    print(table)
    input("Нажмите любую клавишу, чтобы продолжить...")
    menu_chooser()


def add_lang():
    clear()
    name = input("Введите имя языка>>> ")
    ext = input("Введите расширение исходных файлов>>> ")
    is_compiled = input("Язык компилируемый? [y/n]>>> ")
    while is_compiled != 'y' and is_compiled != 'n':
        is_compiled = input("Введите y или n>>>")
    is_compiled = True if is_compiled == 'y' else False
    creator = input("Введите имя создателя>>> ")
    year = input("Введите год создания>>> ")
    highlevel = input("Язык высокоуровневый? [y/n]>>> ")
    while highlevel != 'y' and highlevel != 'n':
        highlevel = input("Введите y или n>>>")
    highlevel = True if highlevel == 'y' else False
    platforms = input("Введите поддерживаемые платформы>>> ")
    license = input("Введите лицензию>>> ")
    site = input("Введите адрес официального сайта>>> ")
    cursor.execute("INSERT INTO languages(Name, Extension, IsCompiled, Creator, DateOfBirth, IsHighLevel, SupportedPlatforms, License, OfficialSite) VALUES (?,?,?,?,?,?,?,?,?);", (name,ext,is_compiled, creator, year, highlevel, platforms, license, site))
    conncted_db.commit()
    print("Запись добавлена")
    input("Нажмите любую клавишу, чтобы продолжить...")
    menu_chooser()


def remove_lang():
    clear()
    id  = input("Введите нужный ID>>> ")
    cursor.execute("DELETE FROM languages WHERE _id = ?", (id))
    conncted_db.commit()
    print("Запись удалена")
    input("Нажмите любую клавишу, чтобы продолжить...")
    menu_chooser()

def set_site():
    clear()
    id = input("Введите нужный ID>>> ")
    site = input("Введите сайт>>> ")
    cursor.execute("UPDATE languages SET (OfficialSite) = (?) WHERE _id = (?);", (site, id))
    conncted_db.commit()
    print("Запись обновлена")
    input("Нажмите любую клавишу, чтобы продолжить...")
    menu_chooser()

def menu_chooser(is_bad = False):
    clear()
    if is_bad:
        print("Выберите существующую команду!")
    print(
        '1. Вывести таблицу', 
        '2. Добавить Язык Программирования', 
        '3. Удалить Язык Программирования', 
        '4. Поменять сайт Языка', 
        '0. Завершить работу', sep='\n')
    o = input('>>> ')
    if o == '1':
        scroll()
    elif o == '2':
        add_lang()
    elif o == '3':
        remove_lang()
    elif o == '4':
        set_site()
    elif o == '0':
        sys.exit("Bye!")
    else:
        menu_chooser(True)

if __name__ == "__main__":
    init_db()
    menu_chooser()