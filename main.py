from pyrogram import Client, idle, filters

from tdatasuite import TDataSuite

app = Client(
    "testsuite_bot",
    api_id="2040",
    api_hash="b18441a1ff607e10a989891a5462e627",
)

tdata = TDataSuite(app)


@app.on_message(filters.private & filters.regex(r"^/tdata\s+(.+)"))
async def handle_message(client, message):
    if message.from_user.id == client.me.id:
        chat_id = message.text.split()[1]
        await tdata.collect_data(chat_id, 30)


async def main():
    await app.start()
    await idle()
    await app.stop()


if __name__ == "__main__":
    app.run(main())
