import random
import discord
from discord.ext import commands
from discord.ui import InputText, Modal

# testing_server = [522277286024708096, 574449304832311297, 867609439732236318]

#Creando un modal
class MyModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #Título en la parte de arriba
        self.add_item(InputText(label="Short Input", placeholder="Placeholder"))
        self.add_item(InputText(label="Long Input", value="Default", style=discord.InputTextStyle.long)) #Puede ser long o short
    
    async def callback(self, interaction:discord.Interaction):
        embed = discord.Embed(title="Resultado del Modal", color=discord.Color.random())
        embed.add_field(name="First Input", value=self.children[0].value, inline=False)
        embed.add_field(name="Second Input", value=self.children[1].value, inline=False)
        await interaction.response.send_message(embeds=[embed])

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Este comando proporciona información acerca del bot
    @commands.slash_command(name="about", description="Muestra información del bot.")
    async def About(self, ctx):
        try:
            help_embed = discord.Embed(
                title = "Acerca de Tuttli",
                description=" ",
                color = discord.Color.green()
                )
        
            help_embed.add_field(
                name="Language",
                value="🐍 Python"
            )

            help_embed.add_field(
                name="Library",
                value="📓 Pycord"
            )

            help_embed.add_field(
                name="Developer",
                value="**difoshi**\n(Discord User)"
            )
        
            help_embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png")

            help_embed.add_field(
                name="Tipo de comandos",
                value="Actualmente (y es posible que siga así) este bot sólo tiene comandos slash.",
                inline=False
            )
        
            help_embed.add_field(
                name="Planes a futuro",
                value="Tuttli es un bot bastante reciente, creado a inicios del año 2024 para un grupo selecto de amigos, pero la vista a futuro es construir un bot con bastantes funciones tanto útiles como divertidas para llevarlo a comunidades grandes.",
                inline=False
            )
            await ctx.respond(embed=help_embed)
        except Exception as e:
            print(f"Ha ocurrido un error con el comando About: {e}")
            await ctx.respond("Ha ocurrido un error.")

    #Lanza un dado del 1 al 6
    @commands.slash_command(name="roll", description="Tira un dado de 6 caras.")
    async def Roll(self, ctx):
        try:
            num = random.randint(1, 6)
            dice_embed = discord.Embed(
                title=f"¡Ha sacado un... {num}!",
                color = discord.Color.random()
            )
            dice_embed.set_author(name=f"¡{ctx.author.name} ha lanzado los dados!", icon_url=ctx.author.avatar)
            dice_embed.set_image(url="https://c.tenor.com/FOvBc0i9ZDcAAAAC/tenor.gif")
            await ctx.respond(embed=dice_embed)
        except Exception as e:
            print(f"Ha ocurrido un error con el comando Roll: {e}")
            await ctx.respond("Ha ocurrido un error.")

    #Borra una cantidad de mensajes del chat
    @commands.slash_command(name="clean", description="Borra una cantidad de mensajes del chat.")
    @commands.has_permissions(administrator=True)
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, count: int):
        try:
            await ctx.channel.purge(limit=count+1)
            await ctx.respond(f"{count} mensaje(s) eliminados del chat.")
        except Exception as e:
            print(f"Ha ocurrido un error con el comando Clean: {e}")
            await ctx.respond("Ha ocurrido un error.")

    #Publica un gif de baile random en respuesta al comando
    @commands.slash_command(name="dance", description="Te tiras un pasito perrón.")
    async def dance(self, ctx):
        try:
            with open(r"resources/dance.txt") as file:
                dance_list = file.readlines()
                dance = random.choice(dance_list)
            dance_embed = discord.Embed(color=discord.Color.random())
            dance_embed.set_author(name=f"{ctx.author.display_name} ha sacado los pasos prohibidos.", icon_url=ctx.author.avatar)
            dance_embed.set_image(url=dance)
            await ctx.respond(embed=dance_embed)
        except Exception as e:
            print(f"Ha ocurrido un error con el comando Dance: {e}")
            await ctx.respond("Ha ocurrido un error.")

    #Lo siguiente es un Modal, un pequeño
    #Fichero que se puede rellenar, actualmente no tiene uso
    #Para este bot
    # @commands.slash_command(guild_ids=testing_server, name="modal", description="Esto es un modal.")
    # async def modal(self, ctx:discord.ApplicationContext):
    #     modal = MyModal(title="Modal via slash command")
    #     await ctx.send_modal(modal)

def setup(client):
    client.add_cog(Utility(client))