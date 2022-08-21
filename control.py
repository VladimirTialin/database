from ui import *
from database import *


def run():
    db = OpenDataBase()
    while True:
        action = Menu()
        if action is None:
            return
        match action:
            case "Все записи":
                ShowAndChoiceData(GetAllPersons(db), "Все записи")
            case " Добавить ":
                newData = InputData()
                if newData is not None:
                    AddPerson(db, newData[0], newData[1],
                              newData[2], newData[3],newData[4])
                SaveDataBase(db)
            case " Изменить ":
                num = GetChanged(GetAllPersons(db))
                GetChangeData(db,num)
                SaveDataBase(db)
            case " Удалить  ":
                id = GetRemoveID(GetAllPersons(db))
                RemovePerson(db, id)
                SaveDataBase(db)
            case "  Фильтр  ":
                filterValue = GetFilterValue()
                if filterValue is not None:
                    ShowAndChoiceData(GetFilterPerson(db, filterValue), f"Отфильтрованные записи по '{filterValue}'")
            case "Отделы":
                ShowDirectory(GetAllDepartments(db), "Справочник отделов")
            case "Должности":
                ShowDirectory(GetAllPositions(db), "Справочник должностей")
            case _:
                print(action)