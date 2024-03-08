from typing import List, Optional
from django.db import models
from django_pydantic_field import SchemaField
from pydantic import BaseModel, RootModel


class SampleItem(BaseModel):
    key: str
    value: str


class SampleArraySchema(RootModel[List[SampleItem]]):
    root: List[SampleItem]

    def append(self, item: SampleItem):
        self.root.append(item)

    def __iter__(self):
        return iter(self.root)

    def __len__(self):
        return len(self.root)

    def __getitem__(self, item):
        return self.root[item]


class SampleModel(models.Model):
    title = models.CharField(max_length=255)
    json: Optional[SampleArraySchema] = SchemaField(blank=True, null=True)
