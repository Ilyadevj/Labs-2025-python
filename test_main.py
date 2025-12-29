# test_main.py
import unittest
from main import (
    Database,
    Procedure,
    ProcedureDatabase,
    build_one_to_many,
    build_many_to_many,
    query_b1,
    query_b2,
    query_b3,
)


class TestProcedures(unittest.TestCase):
    def setUp(self):
        self.databases = [
            Database(1, "HR_DB"),
            Database(2, "Finance_DB"),
            Database(3, "Analytics_DB"),
            Database(4, "Common_DB"),
        ]
        self.procedures = [
            Procedure(1, "GetUsers", 120, 1),
            Procedure(2, "CalcSalary", 180, 2),
            Procedure(3, "ReportGen", 90, 3),
            Procedure(4, "LogCleanup", 60, 4),
            Procedure(5, "BackupProc", 150, 4),
            Procedure(6, "DataMov", 200, 3),
        ]
        self.procedures_databases = [
            ProcedureDatabase(1, 1),
            ProcedureDatabase(2, 2),
            ProcedureDatabase(3, 3),
            ProcedureDatabase(4, 4),
            ProcedureDatabase(5, 4),
            ProcedureDatabase(6, 3),
            ProcedureDatabase(3, 4),
            ProcedureDatabase(4, 1),
        ]

    def test_build_one_to_many(self):
        """Тест построения отношения один-ко-многим"""
        result = build_one_to_many(self.databases, self.procedures)
        self.assertEqual(len(result), 6)  # 6 процедур, каждая привязана к одной базе
        self.assertTrue(all(isinstance(item, tuple) for item in result))
        
        for name, size, db in result:
            self.assertIsInstance(name, str)
            self.assertIsInstance(size, int)
            self.assertIsInstance(db, str)

    def test_query_b1_sorted_by_name(self):
        """Тест запроса Б1: сортировка по имени процедуры"""
        one_to_many = build_one_to_many(self.databases, self.procedures)
        result = query_b1(one_to_many)
        
        names = [item[0] for item in result]
        self.assertEqual(names, sorted(names))
        
        # Проверяем, что все элементы на месте
        self.assertEqual(len(result), 6)

    def test_query_b3_filter_by_proc_suffix(self):
        """Тест запроса Б3: фильтрация по окончанию 'Proc'"""
        many_to_many = build_many_to_many(
            self.databases, self.procedures, self.procedures_databases
        )
        result = query_b3(many_to_many)
        
        self.assertTrue(all(name.endswith("Proc") for name, _ in result))
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "BackupProc")
        
        self.assertIn(result[0][1], ["Analytics_DB", "Common_DB"])


if __name__ == "__main__":
    unittest.main()