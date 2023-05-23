#!/usr/bin/python3
"""
test cases for base model
"""

import unittest
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    def test_initialization(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
