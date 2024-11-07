# app.py
def process_input(user_input):
    # Potentially vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

# test_app.py
import unittest
from app import process_input

class TestApp(unittest.TestCase):
    def test_process_input(self):
        result = process_input("admin")
        self.assertIn("admin", result)

