

import os
import discord
from core.datetime__ import (
    get_current_datetime
)
from core.json__ import (
    read_json_from_file
)


token_json_path = "token.json"
bot_token_json = read_json_from_file(token_json_path)
bot_token = bot_token_json["token"]

client = discord.Client()

discord_bot_trigger_character = "!"

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(f"{discord_bot_trigger_character}kratos"):
        await message.channel.send("Hello im Kratos from another world!")

    elif message.content == f"{discord_bot_trigger_character}datetime":
        await message.channel.send(f"Current datetime: {get_current_datetime()}")

    elif message.content == f"{discord_bot_trigger_character}carmen":
        await message.channel.send("who is Carmen?")



client.run(bot_token)
