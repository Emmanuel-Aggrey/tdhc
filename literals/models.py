from django.db import models
from core.models import BaseModel
# Create your models here.


class BaseLiterals(BaseModel):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Group(BaseLiterals):
    pass


class Status(BaseLiterals):
    pass


class Location(BaseLiterals):
    pass
