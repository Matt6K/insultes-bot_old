import discord

client = discord.Client()

async def send_message(message, channel=None):
    if type(message) != list:
        messages = []
        messages.append(message)
    else:
        messages = message
    for msg in messages:
        if channel:
            await client.send_message(channel, msg)
        else:
            await client.send_message(client.channel, msg)

async def change_game(game):
    await client.change_presence(game=game)

async def change_nickname(user, nickname):
    try:
        await client.change_nickname(user, nickname)
    except discord.errors.Forbidden:
        raise
