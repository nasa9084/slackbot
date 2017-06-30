import os

from peewee import * # NOQA

db = SqliteDatabase(os.path.join(os.path.dirname(__file__), 'lunch.db'))


class Lunch(Model):
    """
    ランチのお店リストを保存するモデル
    """
    name = CharField(primary_key=True)

    class Meta:
        database = db


db.connect()
db.create_tables([Lunch], safe=True)
