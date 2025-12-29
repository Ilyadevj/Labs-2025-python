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


def build_one_to_many(databases, procedures):
    return [
        (p.name, p.size, d.name)
        for d in databases
        for p in procedures
        if p.database_id == d.id
    ]


def build_many_to_many(databases, procedures, procedures_databases):
    many_to_many_temp = [
        (d.name, pd.database_id, pd.procedure_id)
        for d in databases
        for pd in procedures_databases
        if d.id == pd.database_id
    ]

    return [
        (p.name, db_name)
        for db_name, db_id, proc_id in many_to_many_temp
        for p in procedures
        if p.id == proc_id
    ]


def query_b1(one_to_many):
    return sorted(one_to_many, key=lambda x: x[0])


def query_b2(one_to_many, databases):
    res = []
    for d in databases:
        count = len([item for item in one_to_many if item[2] == d.name])
        if count > 0:
            res.append((d.name, count))
    res.sort(key=lambda x: x[1])
    return res


def query_b3(many_to_many):
    return sorted(
        [(name, db) for name, db in many_to_many if name.endswith("Proc")],
        key=lambda x: x[0]
    )


def main():
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

    one_to_many = build_one_to_many(databases, procedures)
    many_to_many = build_many_to_many(databases, procedures, procedures_databases)

    print("--- Запрос Б1 ---")
    print("Список связанных процедур и баз данных (1:M), отсортированный по имени процедуры:")
    for proc, size, db in query_b1(one_to_many):
        print(f"  Процедура: {proc}, Размер: {size} строк, База: {db}")

    print("\n--- Запрос Б2 ---")
    print("Список баз данных с количеством процедур, отсортированный по количеству:")
    for name, count in query_b2(one_to_many, databases):
        print(f"  База данных: {name}, Количество процедур: {count}")

    print("\n--- Запрос Б3 ---")
    print("Список процедур, название которых заканчивается на 'Proc', и базы данных (M:M):")
    for proc, db in query_b3(many_to_many):
        print(f"  Процедура: {proc}, База данных: {db}")


if __name__ == "__main__":
    main()