import os
import sys
from telethon import TelegramClient, events

# API credentials (You need to get these from my.telegram.org)
api_id = "29323596"
api_hash = "db7e9bba180da6f2a2f77fd848e81b12"
bot_token = "8076401841:AAHufvXtGOXJsEQ_owYfqXml0n1WcFwFigA"

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
DATA_FILE_PATH = os.path.join(SCRIPT_DIR, "data.txt")

# Initialize the bot
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Event handler for receiving documents
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Send me the `data.txt` file, and I will replace the old one.")

# Event handler for file upload
@client.on(events.NewMessage(func=lambda e: e.document))
async def handle_document(event):
    document = event.message.document

    # Ensure it's a text file named data.txt
    if document.mime_type == "text/plain" and document.attributes[0].file_name == "data.txt":
        # Remove the previous data.txt file if it exists
        if os.path.exists(DATA_FILE_PATH):
            os.remove(DATA_FILE_PATH)

        # Download the new data.txt file
        await client.download_media(document, file=DATA_FILE_PATH)

        # Send a confirmation message
        await event.reply("The previous `data.txt` has been replaced with the new one.")
    else:
        await event.reply("Please send a valid `data.txt` file.")

# Start the client
client.run_until_disconnected()