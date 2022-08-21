import json
from easygui import *

def OpenDataBase():
    try:
        with open(r"C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork8/employee-database.json", "r", encoding="utf-8") as fh:
            db = json.load(fh)
            db["persons"] = {int(k): v for k, v in db["persons"].items()}
            db["departments"] = {
                int(k): v for k, v in db["departments"].items()}
            db["positions"] = {int(k): v for k, v in db["positions"].items()}
            return db
    except:
        return {"persons": {}, "departments": {}, "positions": {}}

def SaveDataBase(directory):
    with open(r"C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork8/employee-database.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(directory, ensure_ascii=False))

def GetDepartmentID(database, department):
    if department in [n[0] for n in database["departments"].values()]:
        for k, v in database["departments"].items():
            if department == v[0]:
                return int(k)
    else:
        return None

def AddDepartment(database, department):
    departmentID = GetDepartmentID(database, department)
    if departmentID is None:
        if len(database["departments"]) == 0:
            departmentID = 1
        else:
            departmentID = max(database["departments"].keys())+1
        database["departments"][departmentID] = [department]
    return int(departmentID)

def GetAllDepartments(database):
    return [(id, node[0]) for id, node in database["departments"].items()]

def GetPositionstID(database, position):
    if position in [n[0] for n in database["positions"].values()]:
        for k, v in database["positions"].items():
            if position == v[0]:
                return k
    else:
        return None

def AddPosition(database, position):
    positionID = GetPositionstID(database, position)
    if positionID is None:
        if len(database["positions"]) == 0:
            positionID = 1
        else:
            positionID = max(database["positions"].keys())+1
        database["positions"][positionID] = [position]
    return positionID

def GetAllPositions(database):
    return [(id, node[0]) for id, node in database["positions"].items()]

def AddPerson(database, name,dateOfBirth, tel, department, position):
    departmentID = AddDepartment(database, department)
    positionID = AddPosition(database, position)
    if len(database["persons"]) == 0:
        personID = 1
    else:
        personID = max(database["persons"].keys())+1
    database["persons"][int(personID)] = [name,dateOfBirth, tel, departmentID, positionID]

def GetPerson(database, id):
    if id in database["persons"]:
        return (
            id,
            database["persons"][id][0],
            database["persons"][id][1],
            database["persons"][id][2],           
            database["departments"][database["persons"][id][3]][0],
            database["positions"][database["persons"][id][4]][0]
        )
    else:
        return None

def GetAllPersons(database):
    return [GetPerson(database, key) for key in database["persons"].keys()]   


def GetFilterPersonID(database, search):
    return [k for k, v in database["persons"].items() if search.lower() in v[0].lower()]


def GetFilterPerson(database, search):
    return [GetPerson(database, k) for k, v in database["persons"].items() if search.lower() in v[0].lower()]


def RemovePerson(database, id):
    database["persons"].pop(id, None)

def GetChangeData(data,id):
    title = "Изменить запись"
    msg='Изменить данные'
    try:
        fieldNames = ["Ф.И.О","Дата рождения","Телефон", "Отдел", "Должность"]
        fieldNames_defs=data["persons"][id]
        departments=data["departments"][fieldNames_defs[3]]
        positions=data["positions"][fieldNames_defs[4]]
        fieldNames_defs[3]=departments[0]
        fieldNames_defs[4]=positions[0]
        data["persons"].pop(id, None)
        result=multenterbox(msg, title, fieldNames, fieldNames_defs)
        departmentID = AddDepartment(data, result[3])
        positionID = AddPosition(data, result[4])
        data["persons"][id] = [result[0],result[1],
                              result[2], departmentID, positionID]
        return data["persons"][id]
    except: return