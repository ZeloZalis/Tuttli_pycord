import random
import discord
from discord.ext import commands

client = discord.Bot()
testing_server = [522277286024708096, 574449304832311297]

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Comando de ayuda, envía un enved con la información de los comandos
    @client.slash_command(name="help", description="Muestra los comandos del bot.")
    async def Help(self, ctx):
        help_embed = discord.Embed(
            title = "Tuttli comandos!",
            description = "A continuación tienes la lista de comandos disponibles de Tuttli:",
            color = discord.Color.green()
            )
        help_embed.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)
        help_embed.add_field(
            name = "$payito, $ehlipin, $yoelito, $urielito, $valki, $luí, $freddy",
            value = "Muestra un gif del respectivo.", inline=False
            )
        await ctx.respond(embed=help_embed)

    #Lanza un dado del 1 al 6
    @client.slash_command(guild_ids=testing_server, name="roll", description="Tira un dado de 6 caras.")
    async def Roll(self, ctx):
        num = random.randint(1, 6)
        await ctx.respond(f"{ctx.author.mention} ha tirado los dados y ha sacado un {num}.")

def setup(client):
    client.add_cog(Utility(client))