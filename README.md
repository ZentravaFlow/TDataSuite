# TDataSuite
TDataSuite: A toolkit for Telegram data collection and analytics

## Python version

```bash
python --version # Python 3.12.8
```

## Install tdatasuite
```bash
pip install tdatasuite
```

## Usage

1. **Initialize the Client**:
   ```python
   from pyrogram import Client
   from tdatasuite import TDataSuite

   app = Client(
    "testsuite_bot",
    api_id="2040",
    api_hash="b18441a1ff607e10a989891a5462e627",
   )
   
   tdata = TDataSuite(app)
   ```  

2. **Extract Messages**:
   ```python
   await tdata.collect_data("-1000000000000", days=7)  # Get data from the last 7 days
   ```

3. **Save Data**:
   The extracted data is automatically saved in a CSV file named `data_username.csv`.

## Example

```python
from pyrogram import Client

from tdatasuite import TDataSuite

app = Client(
    "testsuite_bot",
    api_id="2040",
    api_hash="b18441a1ff607e10a989891a5462e627",
)

tdata = TDataSuite(app)


async def main():
    await app.start()
    await tdata.collect_data("@admin", 1) # Get data from the last 1 day by default
    await app.stop()


if __name__ == "__main__":
    app.run(main())
```

## Example with Command
You can also use the /tdata command in private messages to save messages from a specific chat

```python
from pyrogram import Client, idle, filters
from tdatasuite import TDataSuite

app = Client(
    "testsuite_bot",
    api_id="2040",
    api_hash="b18441a1ff607e10a989891a5462e627",
)

tdata = TDataSuite(app)


@app.on_message(filters.private & filters.regex(r"^/tdata\s+(.+)"))
async def handler_message(client, message):
    if message.from_user.id == client.me.id:
        chat_id = message.text.split()[1]
        await tdata.collect_data(chat_id, 1)


async def main():
    await app.start()
    await idle()
    await app.stop()


if __name__ == "__main__":
    app.run(main())
```
How it works:
Send a private message to the bot with the command /tdata <chat_id> (e.g., /tdata @admin)

## Output

CSV file:
```csv
row,full_name,user_id,user_name,message,date
1, John Doe, 123456789, johndoe, Hello everyone!, 2025-01-20 10:34:56
2, Jane Smith, 987654321, janesmith, How's it going?, 2025-01-25 14:35:10
3, Alex Johnson, 555555555, alexj, Don't forget the meeting!, 2025-02-01 09:12:45
4, Sarah Brown, 111111111, sarahb, See you all tomorrow., 2025-02-10 18:30:15
```
