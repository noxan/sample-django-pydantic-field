from typing import List
from django.db import models
from django_pydantic_field import SchemaField
from pydantic import RootModel


class Pets(RootModel):
    root: List[str] = []

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class PetsModel(models.Model):
    pets: Pets = SchemaField(blank=True, default=Pets())
