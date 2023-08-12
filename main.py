from os import path
import json
from datetime import datetime

file_base = "base.json"
last_id = 0
data = {}



def read_records():
    global last_id, data
    if not path.exists(file_base):
        with open(file_base, "w") as f:
            pass
        return []
    
    with open(file_base, 'r') as f:
        file_content = f.read().strip()
        if not file_content:
            data['notes'] = []
            return data
        data = json.loads(file_content)
        if data:
            for d in data['notes']:
                    if int(d.get('id')) > last_id:
                        last_id = int(d.get('id'))
            return data
    


def show_all():
    with open('base.json', encoding='utf-8') as f:
        file_content = f.read().strip()
        if not file_content:
            print ("Блокнот пуст\n")
        else:
            data = json.loads(file_content)
            for d in data['notes']:
                print('id: ' +  str(d['id']))
                print('head: ' + d['head'])
                print('text: ' + d['text'])
                print('date: ' + d['date'])
                print('')
        


def add_record():
    global last_id, data
    head = str(input ("Введите заголовок заметки: "))
    text = str(input ("Введите текст заметки: "))
    date = str(datetime.now())
    last_id += 1
    id = str(last_id)
    data['notes'].append({
        'id': id,
        'head': head,
        'text': text,
        'date': date
    })
    with open('base.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print ('Запись добавлена \n')
    print()

def check(string):
    for item in data['notes']['items']:
        if string.lower() in str(item['id'].lower()):
            return False
        if string.lower() in str(item['head'].lower()):
            return False
        if string.lower() in str(item['text'].lower()):
            return False
        if string.lower() in str(item['date'].lower()):
            return False
    return True

def search_record():
    global data
    search = (input ("Что будем искать (введите id/заголовок/текст заметки/дату или их часть? "))
    check = True
    
    for item in data['notes']:
        if search.lower() in str(item['id'].lower()):
            print(item)
            check = False
        elif search.lower() in str(item['head'].lower()):
                print(item)
                check = False
        elif search.lower() in str(item['text'].lower()):
                print(item)
                check = False
            
        elif search.lower() in str(item['date'].lower()):
                print(item)
                check = False
                    
    if check:
        print ("Значение не найдено")
        print()

def change():
    global data
    check = False
    search = int(input ("Введите id записи, которую нужно изменить? "))
    for item in data['notes']:
        if int(item['id']) == search:
            print(item)
            answer = int (input ("Вы хотите изменить эту запись?\n" + 
                    "1. Да \n" 
                    "2. Нет, другую \n"
                    "3. Я передумал, ничего не буду менять \n"))
            if (answer == 1):
                    item['head'] = str(input ("Введите заголовок заметки: "))
                    item['text'] = str(input ("Введите текст заметки: "))
                    item['date'] = str(datetime.now())
                    with open('base.json', 'w', encoding="utf-8") as f:
                        json.dump(data, f, indent=2)
                    print("Запись изменена \n")
                    print('\n')
                    check = True
            if (answer == 2):
                    change()
            if (answer == 3):
                    main_menu()
    if not check:
        print("Запись не найдена\n")
    



def delete():
    global  data
    check = False

    search = int(input ("Введите id записи, которую нужно удалить? "))
    for i in range(len(data['notes'])):
        if int(data['notes'][i]['id']) == search:
            print(data['notes'][i])
            answer = int (input ("Вы хотите удалить эту запись?\n" + 
                "1. Да \n" 
                "2. Нет \n"))
            if (answer == 1):
                del data['notes'][i]
                with open('base.json', 'w', encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
                    print("Запись удалена \n")
                    print('\n')
                    check = True
            if (answer == 2):
                main_menu()
    if not check:
        print("Запись не найдена\n")
    


def delete_all():
    global last_id, data
    answer = int (input("Вы уверены:\n"
                       "1. Да\n"
                       "2. Нет\n"))
    if answer == 1:              
        file = open('base.json', 'w')
        last_id = 0
        data.clear()
        file.close()
        


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Блокнот:\n"
                       "1. Показать все записи\n"
                       "2. Добавить запись\n"
                       "3. Найти запись\n"
                       "4. Изменить запись\n"
                       "5. Удалить запись\n"
                       "6. Очистить блокнот\n"
                       "7. Выйти из программы\n")
                       
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search_record()
            case "4":
                change()
            case "5":
                delete()
            case "6":
                delete_all()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()