from peewee import Model, CharField, IntegerField
from playhouse.db_url import connect
from sanic import Sanic
from sanic.response import json
import os


app = Sanic()
db = connect(os.environ.get('DATABASE_URL') or 'mysql+pool://root@localhost/heroes')


class Heroes(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    identity = CharField()
    hometown = CharField()
    age = IntegerField()

    class Meta:
        database = db


@app.get('/heroes')
async def read(request):
    return json(Heroes.select().dicts())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False, workers=4, access_log=False)
