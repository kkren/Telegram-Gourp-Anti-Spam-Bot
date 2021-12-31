from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import (ChatPermissions)
import challenge
from redisInstance import redis_instance
from dbInstance import db_instance
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

redis = redis.Redis()

app = Client("my_account")

sessions = {}

@app.on_chat_member_updated()
async def challenge_user(client, message):
    if not bool(message.new_chat_member) or bool(message.old_chat_member) or message.chat.type == "channel":
        return
    target = message.new_chat_member.user
        # 新加入群的用户
    chat = message.chat
    try:
        await client.restrict_chat_member(
            chat_id=chat.id,
            user_id=target.id,
            permissions=ChatPermissions()
        )
    except ChatAdminRequired as e:
        return
def allow_user(session):
    app.promote_chat_member()
