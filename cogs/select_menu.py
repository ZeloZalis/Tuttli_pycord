from discord.ext import commands
import discord
from discord.ui import Select, View

testing_server = [522277286024708096, 574449304832311297]

class SelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(guild_ids=testing_server, name="amikos", description="Despliega una lista de amikos.")
    async def Amikos(self, ctx):
        menu = Select(
            # min_values=1, #Cantidad mínima de opciones a seleccionar
            # max_values=3, #Cantidad máxima
            placeholder="Lista de amikos",
            options=[
                discord.SelectOption(label="Payito", emoji="🦔", description="Muestra un gif de payito."), #default=True
                discord.SelectOption(label="Urielito", description="Muestra un gif de urielito."),          #Sirve para mostrar una opción
                discord.SelectOption(label="Yes", description="Muestra un gif de ye."),                     #Por defecto
                discord.SelectOption(label="Freddy", description="Muestra un gif de fredo."),
                discord.SelectOption(label="Luí", description="Muestra un gif de luí."),
                discord.SelectOption(label="Ehlípin", description="Muestra un gif de ehlipin."),
                discord.SelectOption(label="Yoelito", description="Muestra un gif de yoelito."),
                discord.SelectOption(label="Valki Talki", description="Muestra un gif de valkita."),
                discord.SelectOption(label="Pikacuin", description="Muestra un gif del pikacuin.")
            ]
            # row=1 #Se utiliza para cuando haya más de una opción y necesitemos posiciones específicas
        )
        show_menu = View()
        show_menu.add_item(menu)
        await ctx.respond("Escoge una opción.", view=show_menu)

def setup(client):
    client.add_cog(SelectMenu(client))