class Procedure:
    def __init__(self, id, name, size, database_id):
        self.id = id
        self.name = name
        self.size = size
        self.database_id = database_id


class Database:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProcedureDatabase:
    def __init__(self, procedure_id, database_id):
        self.procedure_id = procedure_id
        self.database_id = database_id


# --- Тестовые данные ---
databases = [
    Database(1, "HR_DB"),
    Database(2, "Finance_DB"),
    Database(3, "Analytics_DB"),
    Database(4, "Common_DB"),
]

procedures = [
    Procedure(1, "GetUsers", 120, 1),
    Procedure(2, "CalcSalary", 180, 2),
    Procedure(3, "ReportGen", 90, 3),
    Procedure(4, "LogCleanup", 60, 4),
    Procedure(5, "BackupProc", 150, 4),
    Procedure(6, "DataMov", 200, 3),
]

procedures_databases = [
    ProcedureDatabase(1, 1),
    ProcedureDatabase(2, 2),
    ProcedureDatabase(3, 3),
    ProcedureDatabase(4, 4),
    ProcedureDatabase(5, 4),
    ProcedureDatabase(6, 3),
    ProcedureDatabase(3, 4),
    ProcedureDatabase(4, 1),
]


def main():
    # --- 1) Один-ко-многим ---
    one_to_many = [
        (p.name, p.size, d.name)
        for d in databases
        for p in procedures
        if p.database_id == d.id
    ]

    print("--- Запрос Б1 ---")
    print("Список связанных процедур и баз данных (1:M), отсортированный по имени процедуры:")
    res1 = sorted(one_to_many, key=lambda x: x[0])
    for proc, size, db in res1:
        print(f"  Процедура: {proc}, Размер: {size} строк, База: {db}")

    # --- 2) Количество процедур в каждой базе ---
    print("\n--- Запрос Б2 ---")
    print("Список баз данных с количеством процедур, отсортированный по количеству:")

    res2 = []
    for d in databases:
        count = len(list(filter(lambda x: x[2] == d.name, one_to_many)))
        if count > 0:
            res2.append((d.name, count))

    res2.sort(key=lambda x: x[1])
    for name, count in res2:
        print(f"  База данных: {name}, Количество процедур: {count}")

    # --- 3) Многие-ко-многим ---
    print("\n--- Запрос Б3 ---")
    print("Список процедур, название которых заканчивается на 'Proc', и базы данных (M:M):")

    many_to_many_temp = [
        (d.name, pd.database_id, pd.procedure_id)
        for d in databases
        for pd in procedures_databases
        if d.id == pd.database_id
    ]

    many_to_many = [
        (p.name, db_name)
        for db_name, db_id, proc_id in many_to_many_temp
        for p in procedures
        if p.id == proc_id
    ]

    res3 = sorted(
        [(name, db) for name, db in many_to_many if name.endswith("Proc")],
        key=lambda x: x[0]
    )

    for proc, db in res3:
        print(f"  Процедура: {proc}, База данных: {db}")


if __name__ == "__main__":
    main()
