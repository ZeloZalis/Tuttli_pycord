import discord
import requests
from discord.ext import commands

servers = [522277286024708096, 867609439732236318, 1209660769046761552]

class dollarAPI(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Este es el comando para solicitar a la API del dolar
    #La información de los precios actuales
    @commands.slash_command(guild_ids=servers, name="dolar", description="Muestra los precios del dolar en Venezuela.")
    async def Dolar(self, ctx):
        await ctx.defer()
        try:
            #Se realizarán 3 llamados a APIs que tomarán el precio de Binance, EnParalelo y BCV
            get_enparalelo = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar/unit/enparalelovzla')
            data_enparalelo = get_enparalelo.json()

            get_bcv = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar?page=bcv')
            data_bcv = get_bcv.json()

            get_binance = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar/unit/binance')
            data_binance = get_binance.json()  

            #Con esto, tomaremos la información de la fecha en la que se hace el llamado para
            #Luego imprimirla en el footer
            request_date = data_bcv['datetime']['date']

            dolar_embed = discord.Embed(title="Precio del Dolar en Venezuela", color=discord.Color.random())
            dolar_embed.add_field(name="BCV:", value=f"{data_bcv['monitors']['usd']['price']} VEF")
            dolar_embed.add_field(name="Binance:", value=f"{data_binance['price']} VEF")
            dolar_embed.add_field(name="EnParaleloVnzl:", value=f"{data_enparalelo['price']} VEF")
            dolar_embed.set_image(url="https://c.tenor.com/NpGpS5lm0ekAAAAC/tenor.gif")
            dolar_embed.set_footer(
                text=f"{request_date.capitalize()}, {data_bcv['datetime']['time']}",
                icon_url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png"
                )
            await ctx.respond(embed=dolar_embed)
        except Exception as e:
            print(f"Ha ocurrido un error: {e}.")
            await ctx.respond("Ha ocurrido un error.")

def setup(client):
    client.add_cog(dollarAPI(client))