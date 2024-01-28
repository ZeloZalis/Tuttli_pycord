import random
import discord
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]

class SelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #El siguiente comando abre un menú desplegable
    @commands.slash_command(guild_ids=testing_server, name="amikos", description="Despliega una lista de amikos.")
    async def Amikos(self, ctx):
        
        #Esta clase crea la lista de opciones, con sus descripciones y valores
        class MyView(discord.ui.View):
            @discord.ui.select(placeholder="Lista de amikos", options=[
                discord.SelectOption(label="Payito", value="payito", emoji="🦔", description="Muestra un gif de payito."),
                discord.SelectOption(label="Urielito", value="urielito", emoji="🌈", description="Muestra un gif de uriel."),
                discord.SelectOption(label="Yes", value="ye", emoji="👽", description="Muestra un mensaje de ye."),
                discord.SelectOption(label="Freddy", value="freddy", emoji="💩", description="Muestra un gif de fredi."),
                discord.SelectOption(label="Luí", value="lui", emoji="🐁", description="Muestra un gif de luí."),
                discord.SelectOption(label="Ehlípin", value="ehlipin", emoji="👃", description="Muestra un gif de ehlipin."),
                discord.SelectOption(label="Yoelito", value="yoelito", emoji="👨🏿‍🦲", description="Muestra un gif de yoelito."),
                discord.SelectOption(label="Valki Talki", value="valki", emoji="🐸", description="Muestra un gif de valkita."),
                discord.SelectOption(label="Pikacuin", value="pikacuin", emoji="🔫", description="Muestra un gif del pikacuin.")
            ])
            #El callback se utiliza para ejecutar una función de acuerdo a la opción seleccionada
            #En este caso, va a usar el valor de la opción seleccionada para abrir
            #Un fichero que contiene una lista de gifs
            #Y con el comando random.choice() seleccionará un gif al azar para enviarlo
            async def select_callback(self, select, interaction):
                print(select.values[0])
                with open(f"resources/{select.values[0]}.txt", "r") as file:
                    response_list = file.readlines()
                    response = random.choice(response_list)
                    await interaction.response.send_message(response)
        view = MyView()
        await ctx.respond("Escoge una opción.", view=view)

def setup(client):
    client.add_cog(SelectMenu(client))