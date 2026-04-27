"""
Домашнее задание 3. Задание 2.
Функция для генерации шапки процессуального документа (в арбитражный суд).

На вход подаётся словарь с данными ответчика и номером дела.
По коду из номера дела (например, "А60" в "А60-12345/2025") выбирается
соответствующий арбитражный суд из справочника courts.json.

Данные истца — мои собственные реквизиты (указываются в I_AM ниже).

Вторая функция принимает список словарей с ответчиками и печатает
в консоль все сгенерированные шапки через цикл for.
"""

import json
import os


# Справочник арбитражных судов по двухзначному коду субъекта
# (код суда — первые 3 символа номера дела, например "А60").
_COURTS_PATH = os.path.join(os.path.dirname(__file__), "courts.json")
with open(_COURTS_PATH, encoding="utf-8") as f:
    COURTS = json.load(f)

# Мои данные (истец). При желании замените на свои реальные реквизиты.
I_AM = {
    "name": "Пигин Максим Сергеевич",
    "inn": "7701234567",
    "ogrnip": "318774600123456",
    "address": "101000, г. Москва, ул. Мясницкая, д. 20",
}


def get_court_by_case(case_number: str) -> dict:
    """Возвращает словарь с реквизитами суда по номеру дела.

    Код суда — это символы до первого дефиса (например, 'А60' из 'А60-12345/2025').
    """
    if not case_number or "-" not in case_number:
        raise ValueError(f"Некорректный номер дела: {case_number!r}")
    court_code = case_number.split("-", 1)[0].strip()
    court = COURTS.get(court_code)
    if court is None:
        raise KeyError(f"Суд с кодом {court_code!r} не найден в справочнике")
    return court


def build_header(defendant: dict) -> str:
    """Формирует шапку процессуального документа.

    Аргумент:
        defendant — словарь с ключами:
            name, inn, ogrn, address, case_number

    Возвращает готовую шапку в виде строки.
    """
    required = {"name", "inn", "ogrn", "address", "case_number"}
    missing = required - set(defendant)
    if missing:
        raise KeyError(f"В данных ответчика нет полей: {missing}")

    court = get_court_by_case(defendant["case_number"])

    header = (
        f"В {court['name']}\n"
        f"Адрес: {court['address']}\n"
        f"\n"
        f"Истец: {I_AM['name']}\n"
        f"ИНН {I_AM['inn']} ОГРНИП {I_AM['ogrnip']}\n"
        f"Адрес: {I_AM['address']}\n"
        f"\n"
        f"Ответчик: {defendant['name']}\n"
        f"ИНН {defendant['inn']} ОГРН {defendant['ogrn']}\n"
        f"Адрес: {defendant['address']}\n"
        f"\n"
        f"Номер дела {defendant['case_number']}"
    )
    return header


def print_headers_for_all(defendants: list) -> None:
    """Печатает шапки для всех ответчиков из списка."""
    for i, defendant in enumerate(defendants, start=1):
        print(f"===== Шапка №{i} =====")
        print(build_header(defendant))
        print()


# --- Демонстрация работы ---
if __name__ == "__main__":
    defendants = [
        {
            "name": "ООО «Кооператив Озеро»",
            "inn": "1231231231",
            "ogrn": "123124129312941",
            "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69",
            "case_number": "А40-123456/2023",
        },
        {
            "name": "ООО «Альфа-Строй»",
            "inn": "7701234567",
            "ogrn": "1027700123456",
            "address": "г. Москва, ул. Строителей, д. 15",
            "case_number": "А60-12345/2025",
        },
        {
            "name": "ЗАО «Бета-Инвест»",
            "inn": "7702345678",
            "ogrn": "1037700234567",
            "address": "г. Москва, пр-т Мира, д. 42",
            "case_number": "А56-77777/2025",
        },
    ]

    print_headers_for_all(defendants)
