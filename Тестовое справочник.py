import os
import re
from faker import Faker
import random

SPRAVOCHNIK_FILE: str = "spravochnik.txt"

def input_validate_fio(prompt: str) -> str:
    """
    Функция для проверки корректности ввода ФИО.

    Args:
        prompt: Подсказка для ввода.

    Returns:
        str: Введенное корректное ФИО.
    """
    name: str = input(prompt)
    if not name.replace(" ", "").isalpha():
        print("Некорректное имя. Имя должно состоять только из букв.")
        return input_validate_fio(prompt)
    return name

def print_entry(entry: dict) -> None:
    """
    Функция для вывода записи из справочника.

    Args:
        entry (dict): Словарь с данными записи.
    """
    print(f"{entry['фамилия']} "
          f"{entry['имя']} "
          f"{entry['отчество']},"
          f"{entry['организация']}, "
          f"{entry['телефон_рабочий']}, "
          f"{entry['телефон_личный']}")

def input_phone_number(prompt: str = "Введите номер телефона: ") -> str:
    """
    Функция для ввода и форматирования номера телефона.

    Args:
        prompt (str): Подсказка для ввода.

    Returns:
        str: Форматированный номер телефона.
    """
    phone_number: str = input(prompt)
    # Удаляем все символы, кроме цифр
    digits: str = re.sub(r"\D", "", phone_number)
    # Проверяем, является ли введенная строка числом и длина строки равна 11
    if phone_number.isdigit() and len(phone_number) == 11:
        # Форматируем номер с разделительными "-"
        formatted_number: str = f"{phone_number[:1]}-{phone_number[1:4]}-{phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:11]}"
        return formatted_number
    else:
        print("Некорректный номер телефона. Пожалуйста, введите номер в правильном формате.")
        # Если номер некорректен, вызываем функцию снова, чтобы пользователь мог ввести его заново
        return input_phone_number(prompt)

def add_entry() -> None:
    """
    Функция для добавления записи в справочник.
    """
    entry: dict = {}
    entry['фамилия']: str = input_validate_fio("Введите фамилию: ")
    entry['имя']: str = input_validate_fio("Введите имя: ")
    entry['отчество']: str = input_validate_fio("Введите отчество: ")
    entry['организация']: str = input("Введите название организации: ")
    entry['телефон_рабочий']: str = input_phone_number("Введите рабочий телефон: ")
    entry['телефон_личный']: str = input_phone_number("Введите личный телефон: ")

    with open(SPRAVOCHNIK_FILE, "a") as file:
        file.write(",".join(entry.values()) + "\n")

def search_entry() -> None:
    """
    Функция для поиска записей в справочнике.
    """
    search_query: str = input("Введите строку для поиска: ").lower()
    found_any_entry: bool = False

    with open(SPRAVOCHNIK_FILE, "r") as file:
        for line in file:
            entry: dict = dict(zip(['фамилия', 'имя', 'отчество', 'организация', 'телефон_рабочий', 'телефон_личный'],
                             line.strip().split(",")))
            entry_values: str = " ".join(entry.values()).lower()  # Создаем строку для поиска из всех значений записи
            if any(search_query in value for value in
                   entry_values.split()):  # Проверяем, содержит ли какое-либо из полей записи искомую строку
                print_entry(entry)
                found_any_entry = True

    if not found_any_entry:
        print("Нет записей, содержащих указанную строку.")

def main() -> None:
    """
    Главная функция программы.
    """
    if not os.path.exists(SPRAVOCHNIK_FILE):
        open(SPRAVOCHNIK_FILE, "a").close()

    while True:
        print()
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Поиск записей")
        print("4. Выход")
        choice: str = input("Выберите действие -------------->")
        print()
        if choice == "1":
            with open(SPRAVOCHNIK_FILE, "r") as file:
                for line in file:
                    entry: dict = dict(zip(['фамилия', 'имя', 'отчество', 'организация', 'телефон_рабочий', 'телефон_личный'], line.strip().split(",")))
                    print_entry(entry)
        elif choice == "2":
            add_entry()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()

fake: Faker = Faker(['ru_RU'])

def generate_random_entry() -> dict:
    """
    Функция для генерации случайной записи в справочник.

    Returns:
        dict: Словарь с данными случайной записи.
    """
    entry: dict = {}
    entry['фамилия']: str = fake.last_name()
    entry['имя']: str = fake.first_name()
    entry['отчество']: str = fake.middle_name()
    entry['организация']: str = fake.company()
    entry['телефон_рабочий']: str = fake.phone_number()
    entry['телефон_личный']: str = fake.phone_number()
    return entry

def populate_directory_with_random_data() -> None:
    """
    Функция для генерации и записи случайных данных в справочник.
    """
    with open(SPRAVOCHNIK_FILE, "a") as file:
        for _ in range(100):
            entry: dict = generate_random_entry()
            file.write(",".join(entry.values()) + "\n")

#populate_directory_with_random_data()
