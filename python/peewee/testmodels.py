from peewee import *

database = SqliteDatabase('testDB.sqlite', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Company(BaseModel):
    address = TextField(column_name='ADDRESS', null=True)
    age = IntegerField(column_name='AGE')
    id = AutoField(column_name='ID')
    name = CharField(column_name='NAME')
    salary = FloatField(column_name='SALARY', null=True)

    class Meta:
        table_name = 'COMPANY'

class Department(BaseModel):
    dept = CharField(column_name='DEPT')
    emp = IntegerField(column_name='EMP_ID')
    id = AutoField(column_name='ID')

    class Meta:
        table_name = 'DEPARTMENT'

class N(BaseModel):
    f = TextField(null=True)
    l = TextField(null=True)

    class Meta:
        table_name = 'n'

