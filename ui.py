from easygui import *
from database import*


def Menu():
    text = "Программа предназначена для ведения и учета сотрудников\nВашей компании.\nДля начала работы выберите необходимое меню из списка."
    title = "База данных"
    button_list = [" Добавить "," Изменить "," Удалить  ","  Фильтр  ", "Все записи","Отделы","Должности" ]
    return buttonbox(text, title, button_list)


def InputData():
    msg = "Введите данные о сотруднике"
    title = "Ввод данных"
    fieldNames = ["Ф.И.О","Дата рождения","Телефон", "Отдел", "Должность"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)
    return fieldValues


def ShowAndChoiceData(data, msg):
    choices = ["id | Ф.И.О. | Дата рождения | Телефон | Отдел | Должность", " "] + sorted([f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]}" for item in data])
    return choicebox(msg, msg, choices)

def ShowDirectory(data, msg):
    choices = ["id, Наименование", " "] + [f"{item[0]}, {item[1]}" for item in data]
    return choicebox(msg, msg, choices)


def GetRemoveID(data):
    removeItem = ShowAndChoiceData(data, "Выберите запись для удаления")
    choices = ["Да","Нет"]
    if removeItem is not None:
        if removeItem[0].isdigit():
            if ynbox("Удалить запись?\n" + removeItem,choices=choices):
                id = int(removeItem.split(" | ")[0])
                return id
    return None

def GetFilterValue():
    return enterbox("Введите критерий для фильтрации")

def GetChanged(data):
    removeItem = ShowAndChoiceData(data, "Выберите запись для изменения")
    choices = ["Да","Нет"]
    if removeItem is not None:
        if removeItem[0].isdigit():
            if ynbox("Изменить запись?\n" + removeItem,choices=choices):
                id = int(removeItem.split(" | ")[0])
                return id



    