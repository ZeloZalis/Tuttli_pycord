import discord
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]

class Menu_boton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Presióname", style=discord.ButtonStyle.green)
    async def boton_1(self, interaction:discord.Interaction):
        await interaction.response.send_message("Holi jiijiji", ephemeral=True)

class Boton(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(guild_ids=testing_server, name="botoncito", description="No sé qué hace jiji")
    async def botoncito(self, ctx):
        mi_menu = Menu_boton()
        await ctx.respond(view=mi_menu)

def setup(client):
    client.add_cog(Boton(client))