import discord
import requests
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]

class Wikipedia_API(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids = testing_server, name='wiki', description="Para buscar algo en wikipedia.")
    async def wiki(self, ctx, *, query: str):
        pass

def setup(client):
    client.add_cog(Wikipedia_API(client))