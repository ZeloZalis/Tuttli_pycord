import random
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]

class Gifs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids=testing_server, name="urielito", description="Publica un gif de Uriel.")
    async def Urielito(self, ctx):
        with open(r"resources\urielito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.respond(response)

    @commands.slash_command(guild_ids=testing_server, name="yes", description="Un mensaje para ye.")
    async def Yes(self, ctx):
        await ctx.respond("Ye puto.")
    
    @commands.slash_command(guild_ids=testing_server, name="freddy", description="Publica un gif de Freddy.")
    async def Freddy(self, ctx):
        with open(r"resources\freddy.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.respond(response)

    @commands.slash_command(guild_ids=testing_server, name="luí", description="Publica un gif de Luí.")
    async def Luí(self, ctx):
        await ctx.respond("https://c.tenor.com/yvdqdIeLhFMAAAAd/tenor.gif")
    
    @commands.slash_command(guild_ids=testing_server, name="payito", description="Publica un gif de Payito.")
    async def Payito(self, ctx):
        with open(r"resources\payito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.respond(response)

    @commands.slash_command(guild_ids=testing_server, name="ehlipin", description="Publica un gif de Ehlipin.")
    async def Ehlipin(self, ctx):
        with open(r"resources\ehlipin.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.respond(response)

    @commands.slash_command(guild_ids=testing_server, name="yoelito", description="Publica un gif de Yoelito.")
    async def Yoelito(self, ctx):
        with open(r"resources\yoelito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.respond(response)

    # @client.slash_command(guild_ids=testing_server, name="valkie talkie", description="Publica un gif de Valki.")
    # async def Valki(self, ctx):
    #     with open(r"resources\valki.txt", "r") as file:
    #         response_list = file.readlines()
    #         response = random.choice(response_list)
    #     await ctx.respond(response)

def setup(client):
    client.add_cog(Gifs(client))