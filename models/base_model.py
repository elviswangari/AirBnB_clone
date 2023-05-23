#!/usr/bin/python3
"""
a base model for other classes and methods
"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializes the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of instance"""
        cls = self.__class__.__name__
        return f"[{cls}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the puplic instance updated_at to current date"""
        pass

    def to_dict(self):
        pass
