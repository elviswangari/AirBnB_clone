#!/usr/bin/python3
"""
test cases for base model
"""

import unittest
from models.base_model import BaseModel

base_model = BaseModel()


class BaseModelTestCase(unittest.TestCase):
    def test_initialization(self):
        self.assertIsInstance(base_model.id, str)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_save(self):
        self.assertNotEqual(base_model.created_at,
                            base_model.updated_at, "expected")


if __name__ == '__main__':
    unittest.main()
