import random
import discord
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]
client = discord.Bot()

class SelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #El siguiente comando abre un menú desplegable
    @commands.slash_command(guild_ids=testing_server, name="amikos", description="Despliega una lista de amikos.")
    async def Amikos(self, ctx):
        try:
            #Esta clase crea la lista de opciones, con sus descripciones y valores
            class MyView(discord.ui.View):
                @discord.ui.select(placeholder="Lista de amikos", max_values=1, options=[
                    discord.SelectOption(label="Payito", value="payito", emoji="🦔", description="Muestra un gif de payito."),
                    discord.SelectOption(label="Urielito", value="urielito", emoji="🏳️‍🌈", description="Muestra un gif de uriel."),
                    discord.SelectOption(label="Yes", value="ye", emoji="👽", description="Muestra un mensaje de ye."),
                    discord.SelectOption(label="Freddy", value="freddy", emoji="💩", description="Muestra un gif de fredi."),
                    discord.SelectOption(label="Luí", value="lui", emoji="☢️", description="Muestra un gif de luí."),
                    discord.SelectOption(label="Ehlípin", value="ehlipin", emoji="👃", description="Muestra un gif de ehlipin."),
                    discord.SelectOption(label="Yoelito", value="yoelito", emoji="👨🏿‍🦲", description="Muestra un gif de yoelito."),
                    discord.SelectOption(label="Valki Talki", value="valki", emoji="🐸", description="Muestra un gif de valkita."),
                    discord.SelectOption(label="Pikacuin", value="pikacuin", emoji="🔫", description="Muestra un gif del pikacuin."),
                    discord.SelectOption(label="La pepiña", value="pepiña", emoji="🐁", description="Muestra un gif de la pepiña."),
                    discord.SelectOption(label="Jerry", value="jerry", emoji="🐒", description="Muestra un gif de jerry.")
                ])
                #El callback se utiliza para ejecutar una función de acuerdo a la opción seleccionada
                #En este caso, va a usar el valor de la opción seleccionada para abrir
                #Un fichero que contiene una lista de gifs
                #Y con el comando random.choice() seleccionará un gif al azar para enviarlo
                async def select_callback(self, select, interaction):
                    with open(f"resources/{select.values[0]}.txt", "r") as file:
                        name_solicited = select.values[0]
                        response_list = file.readlines()
                        response = random.choice(response_list)
                    menu_embed = discord.Embed(color=discord.Color.random())
                    menu_embed.set_author(name=f"{ctx.author.name} ha seleccionado a {name_solicited.capitalize()}.", icon_url=ctx.author.avatar)
                    menu_embed.set_image(url=response)
                    menu_embed.set_footer(
                        text="Gracias por usar a Tuttli bot!",
                        icon_url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png"
                        )
                    await interaction.response.send_message(embed=menu_embed)
            view = MyView()
            await ctx.respond("Escoge una opción y mira la magia.", view=view, ephemeral=True)
        except Exception as e:
            print(f"Ha ocurrido un error con el comando Amikos: {e}")
            await ctx.respond("Ha ocurrido un error.")

def setup(client):
    client.add_cog(SelectMenu(client))