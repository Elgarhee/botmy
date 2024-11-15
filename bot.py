import logging
import asyncio
import io
import contextlib
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

api_id = '13508783'
api_hash = '84b6742e711a99caa527393515249899'
bot_token = '7271121948:AAGcP02QCK1TmpmOwZhrkMPvRv-YSKHuZmw'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Send me some Python code and I'll run it for you!")

@app.on_message(filters.text & filters.private)
async def run_code(client, message):
    code = message.text
    
    exec_globals = {}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code, exec_globals)
            result = output.getvalue()
        except Exception as e:
            result = str(e)
    
    await message.reply(result)

if __name__ == "__main__":
    app.run()
