from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    table = models.CharField(max_length=20)


class Region(models.Model):
    name = models.CharField(max_length=10)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name# + "  " + ','.join([str(u) for u in self.users.all()])


class Info(models.Model):
    class Meta:
        abstract = True
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    description = models.TextField()

    def __str__(self):
        return str(self.region)

    TABLES = {}

    @classmethod
    def get_table(cls, name):
        return cls.TABLES[name]

    @classmethod
    def get_table_names(cls):
        return cls.TABLES.keys()

    @classmethod
    def add_table(cls, name, table):
        cls.TABLES[name] = table


class Info1(Info):
    pass

Info.add_table('table1', Info1)

class Info2(Info):
    pass

Info.add_table('table2', Info2)

class Info3(Info):
    pass

Info.add_table('table3', Info3)

