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
        get_dollar = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar/')
        data_dollar = get_dollar.json()
        request_date = data_dollar['datetime']['date']

        dolar_embed = discord.Embed(title="Precio del Dolar en Venezuela", color=discord.Color.random())
        dolar_embed.add_field(name="BCV:", value=f"{data_dollar['monitors']['bcv']['price']} VEF", inline=True)
        dolar_embed.add_field(name="Binance:", value=f"{data_dollar['monitors']['binance']['price']} VEF", inline=True)
        dolar_embed.add_field(name="Cripto Dolar:", value=f"{data_dollar['monitors']['cripto_dolar']['price']} VEF", inline=True)
        dolar_embed.add_field(name="DolarToday:", value=f"{data_dollar['monitors']['dolar_today']['price']} VEF", inline=True)
        dolar_embed.add_field(name="EnParaleloVnzl:", value=f"{data_dollar['monitors']['enparalelovzla']['price']} VEF", inline=True)
        dolar_embed.set_image(url="https://c.tenor.com/NpGpS5lm0ekAAAAC/tenor.gif")
        dolar_embed.set_footer(
            text=f"{request_date.capitalize()}, {data_dollar['datetime']['time']}",
            icon_url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png"
            )
        await ctx.respond(embed=dolar_embed)

    #Este es el comando para solicitar a la API del euro
    #La información de los precios actuales
    @commands.slash_command(guild_ids=servers, name="euro", description="Muestra los precios del euro en Venezuela.")
    async def Euro(self, ctx):
        get_euro = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/euro/')
        data_euro = get_euro.json()
        request_date = data_euro['datetime']['date']

        dolar_embed = discord.Embed(title="Precio del Euro en Venezuela", color=discord.Color.random())
        dolar_embed.add_field(name="BCV:", value=f"{data_euro['monitors']['bcv']['price']} VEF", inline=True)
        dolar_embed.add_field(name="Binance:", value=f"{data_euro['monitors']['binance']['price']} VEF", inline=True)
        dolar_embed.add_field(name="Cripto Euro:", value=f"{data_euro['monitors']['cripto_euro']['price']} VEF", inline=True)
        dolar_embed.add_field(name="EuroToday:", value=f"{data_euro['monitors']['euro_today']['price']} VEF", inline=True)
        dolar_embed.add_field(name="EnParaleloVnzl:", value=f"{data_euro['monitors']['enparalelovzla']['price']} VEF", inline=True)
        dolar_embed.set_image(url="https://c.tenor.com/S2zUB5nC4ZUAAAAd/tenor.gif")
        dolar_embed.set_footer(
            text=f"{request_date.capitalize()}, {data_euro['datetime']['time']}",
            icon_url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png"
            )
        await ctx.respond(embed=dolar_embed)

def setup(client):
    client.add_cog(dollarAPI(client))