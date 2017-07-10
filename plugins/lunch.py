from random import choice

from slackbot.bot import listen_to
from peewee import * # NOQA
from .lunch_model import Lunch


@listen_to('^\$lunch$')
def choose_lunch(message):
    lunch = Lunch.select().order_by(fn.Random()).limit(1)
    if not lunch:
        message.reply('ランチリストがありません')
        return
    message.reply(lunch[0].name)

@listen_to('^\$lunch add (.+)')
def add_lunch(message, lunch):
    try:
        Lunch.create(name=lunch)
    except IntegrityError as e:
        message.reply('ランチリストにすでに{}が存在します。'.format(lunch))
        return
    message.send('ランチリストに{}を追加しました。'.format(lunch))

@listen_to('^\$lunch (remove|delete) (.+)')
def delete_lunch(message, _, lunch):
    lunchobj = Lunch.get(name=lunch)
    lunchobj.delete_instance()
    message.send('ランチリストから{}を削除しました。'.format(lunch))

@respond_to(r'^lunch\s+help+')
def lunch_help(message):
    """
    ヘルプメッセージを返す
    """
    message.send('''- `$lunch`: ランチリストからランダムに一つ返す
- `$lunch add (名前)`: ランチリストにランチの種類を追加する
- `$lunch delete (名前)`: ランチリストからランチの種類を消去する
''')
