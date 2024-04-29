from datetime import date
import os
from classes import Orders, Agency, Storage
fileNameStorage = "travelAgency.txt"
fileNameOrders = "dataTour.txt"
orders=Orders()
storage=Storage()
def options():
    print("1: Список усіх туристичних агенств: ")
    print("2: Спиок доступних турів: ")
    print("3: Додати нове турагенство: ")
    print("4: Додати новий тур: ")
    print("5: Зберегти: ")
    print("6: Пошук туристичних агенств: ")
    print("7: Пошук доступних турів: ")
    print("8: Завершення роботи")

def options_storage_find():
    print("\n~~~~~~ПОШУК ТУРАГЕНСТВ~~~~~~~")
    print("1: Пошук за назвою країни")
    print("2: Пошук за типом подорожі")
    print("3: Повернутися у основне меню")

def options_orders_find():
    print("\n~~~~~ПОШУК ТУРІВ~~~~~")
    print("1: Пошук за номером туру")
    print("2: Пошук за тривалістю туру")
    print("3: Повернутися у основне меню")

storage.read_from_file(fileNameStorage)
orders.read_from_file(fileNameOrders)
os.system('cls')
options()
while True:
    option = int(input("~~~~~~Виберіть пункт меню: "))
    
    if option == 1:
        storage.print("all")
    elif option == 2:
        orders.print()
    elif option == 3:
        name=input("Введіть назву турагенції: ")
        country=input("Введіть країну: ")
        city=input("Введіть місто: ")
        photolist=input("Вкажіть напрям роботи агенства: ")
        category=input("Введіть адресу турагенства (посилання): ")
        storage.add(Agency(name,country,city,photolist,category))
    elif option == 4:
        name=input("Введіть назву турагенції: ")
        date=input("Введіть дату: ")
        days=input("Введіть тривальсть днів: ")
        numberofpeople=input("Введіть кількість людей: ")
        cost=input("Введіть вартість туру: ")
        photo=input("Введіть фото туру: ")
        orders.create(name,date,days,numberofpeople,cost,photo)
    elif option == 5:
        storage.save_to_file(fileNameStorage)
        orders.save_to_file(fileNameOrders)
    elif option == 6:
        os.system('cls')
        while True:
            options_storage_find()
            option = input("--Виберіть пункт меню: ")
            if option == '1': # name                
                country = input ("Введіть назву повністю або частину: ")
                storage.find('country', country)
            elif option == '2':# photolist
                text = input("Введіть характеристику з опису: ")
                storage.find('photolist', text)
            
            elif option == '3':
                os.system('cls')
                options()
                break
            else:
                print("Виберіть коректне значення")
    
    elif option == 7:
        os.system('cls')
        while True:
            options_orders_find()
            option = input("--Виберіть пункт меню: ")
            if option == '1': # order's number
                number = int(input ("Введіть номер туру: "))
                orders.find('number', number)
            elif option == '2':# name
                days = int(input ("Введіть тривалість туру: "))
                orders.find('days', days)
            elif option == '3':
                os.system('cls')
                options()
                break
            else:
                print("Виберіть коректне значення")
    
    elif option == 8:
        break
    else:
        print("Input menu number, pls\n")
print("Роботу завершено")