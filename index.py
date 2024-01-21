import discord
from decouple import config
import os

client = discord.Bot()

@client.event
async def on_ready():
    print(f"I just logged as {client.user}")

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    print(f"Intentando cargar {cogfile}")
    try:
        client.load_extension(cogfile)
    except Exception as e:
        print(f"Error: {e}")

testing_server = [522277286024708096, 574449304832311297]

@client.slash_command(guild_ids=testing_server, name="pinggg", description="Test description")
async def ping(ctx):
    await ctx.respond(f"Mi ping es de {int(client.latency*1000)} ms.")

client.run(config("token"))