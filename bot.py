import uuid

from pyrogram import (Client, filters)
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import (Message, ChatPermissions)
import challenge
from redisInstance import redis_instance
from dbInstance import db_instance
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Client("my_account")

sessions = {}

@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    try:

    if message.from_user.id in sessions:
        await client.send_message(message.chat.id, "You are already in a session.")
        return

@app.on_chat_member_updated()
async def new_user_event(client, message):
    if not bool(message.new_chat_member) or bool(message.old_chat_member) or message.chat.type == "channel":
        return
    target = message.new_chat_member.user
    chat = message.chat
    user_cursor = db_instance.cursor(dictionary=True)
    user_cursor.excute("START TRANSACTION;")
    user_cursor.excute("SELECT * FROM users WHERE user_id = target.id")
    user_result = user_cursor.fetchall()
    if not user_result:
        try:
            user_cursor.excute("INSERT INTO users (user_id, last_challenge_time, last_challenge_group, join_count) VALUES (target.id, 0, 0, 0)")
            user_result['user_id'] = target.id
            user_result['last_challenge_time'] = int(time.time())
            user_result['last_challenge_group'] = 0
            user_result['join_count'] = 0
        except Exception as e:
            await client.send_message(chat.id, "Error: " + str(e))
    try:
        await client.restrict_chat_member(
            chat_id=chat.id,
            user_id=target.id,
            permissions=ChatPermissions()
        )
    except ChatAdminRequired as e:
        return
    user_cursor.excute("COMMIT;")
    try:
        session_key = await challenge.new_challenge(target.id)
    except Exception as e:
        await client.send_message(chat.id, "Error: " + str(e))

def allow_user(session):
    app.promote_chat_member()
