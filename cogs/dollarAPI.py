import discord
import requests
from discord.ext import commands

testing_server = [522277286024708096, 574449304832311297]

class dollarAPI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids=testing_server, name="dolar", description="Muestra los precios del dolar en Venezuela.")
    async def dolar_ve(self, ctx):
        get_dollar = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar/')
        data_dollar = get_dollar.json()

        dolar_embed = discord.Embed(title="Precio del Dolar en Venezuela", color=discord.color.green())
        dolar_embed.add_field(name="BCV:", value=f"{data_dollar['monitors']['bcv']['price']}", inline=True)
        dolar_embed.add_field(name="Binance:", value=f"{data_dollar['monitors']['binance']['price']}", inline=True)
        dolar_embed.add_field(name="Cripto Dolar:", value=f"{data_dollar['monitors']['cripto_dolar']['price']}", inline=True)
        dolar_embed.add_field(name="DolarToday:", value=f"{data_dollar['monitors']['dolar_today']['price']}", inline=True)
        dolar_embed.add_field(name="EnParaleloVnzl:", value=f"{data_dollar['monitors']['enparalelovzla']['price']}", inline=True)
        dolar_embed.set_footer(text="Footer! No markdown here.")







def setup(client):
    client.add_cog(dollarAPI(client))