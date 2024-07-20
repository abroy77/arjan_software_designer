import unittest
from .e1_pure_functions_and_side_effects import weekday, generate_id
from datetime import datetime
import string

class TestWeekday(unittest.TestCase):
    def test_weekday(self):
        self.assertEqual(weekday(), f"{datetime.today():%A}")

class TestGenerateId(unittest.TestCase):
    def test_generate_id_length(self):
        length = 10
        generated_id = generate_id(length)
        self.assertEqual(len(generated_id), length)

    def test_generate_id_characters(self):
        length = 10
        generated_id = generate_id(length)
        allowed_characters = string.ascii_uppercase + string.digits
        for char in generated_id:
            self.assertIn(char, allowed_characters)
    def test_generate_id_repeat(self):
        length = 10
        n = 10
        ids = []
        for _ in range(n):
            new_id = generate_id(length)
            for id in ids:
                self.assertNotEqual(new_id, id)
            ids.append(new_id)
        
