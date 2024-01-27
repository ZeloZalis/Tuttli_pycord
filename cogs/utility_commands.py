import random
import discord
from discord.ext import commands
from discord.ui import InputText, Modal

testing_server = [522277286024708096, 574449304832311297]

#Creando un modal
class MyModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #Título en la parte de arriba
        self.add_item(InputText(label="Short Input", placeholder="Placeholder"))
        self.add_item(InputText(label="Long Input", value="Default", style=discord.InputTextStyle.long)) #Puede ser long o short
    
    async def callback(self, interaction:discord.Interaction):
        embed = discord.Embed(title="Resultado del Modal", color=discord.Color.green())
        embed.add_field(name="First Input", value=self.children[0].value, inline=False)
        embed.add_field(name="Second Input", value=self.children[1].value, inline=False)
        await interaction.response.send_message(embeds=[embed])

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Comando de ayuda, envía un enved con la información de los comandos
    @commands.slash_command(name="help", description="Muestra los comandos del bot.")
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
    @commands.slash_command(guild_ids=testing_server, name="roll", description="Tira un dado de 6 caras.")
    async def Roll(self, ctx):
        num = random.randint(1, 6)
        dice_embed = discord.Embed(
            title=f"¡Ha sacado un... {num}!",
            color = discord.Color.green()
        )
        dice_embed.set_author(name=f"¡{ctx.author.name} ha lanzado los dados!", icon_url=ctx.author.avatar)
        dice_embed.set_image(url="https://c.tenor.com/FOvBc0i9ZDcAAAAC/tenor.gif")
        await ctx.respond(embed=dice_embed)

    #Borra una cantidad de mensajes del chat
    @commands.slash_command(guild_ids=testing_server, name="clear", description="Borra una cantidad de mensajes del chat.")
    @commands.has_role("Mod")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count+1)
        await ctx.respond(f"{count} mensaje(s) eliminados del chat.")

    #Lo siguiente es un Modal, un pequeño
    #Fichero que se puede rellenar, actualmente no tiene uso
    #Para este bot
    @commands.slash_command(guild_ids=testing_server, name="modal", description="Esto es un modal.")
    async def modal(self, ctx:discord.ApplicationContext):
        modal = MyModal(title="Modal via slash command")
        await ctx.send_modal(modal)

def setup(client):
    client.add_cog(Utility(client))