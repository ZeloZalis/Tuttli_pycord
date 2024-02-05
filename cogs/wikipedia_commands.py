import re
import discord
import requests
import wikipedia
from discord.ext import commands

wikipedia.set_lang("es")

testing_server = [522277286024708096, 574449304832311297]

class Wikipedia_API(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids = testing_server, name='wiki', description="Para buscar algo en wikipedia.")
    async def wiki(self, ctx, *, busqueda: str):
        parrafo = {
            'action':'query',
            'format':'json',
            'titles':busqueda,
            'prop':'info',
            'origin':'*'
        }
        request_api = requests.get("https://es.wikipedia.org/w/api.php", params=parrafo)
        data = request_api.json()
        first_page = next(iter(data['query']['pages'].values()))
        the_url = f"https://es.wikipedia.org/?curid={first_page['pageid']}"

        response = wikipedia.summary(busqueda, sentences=2)
        response_clean = re.sub(r'\[\d+\]|\[\d+\]\[.*?\]|\[http.*?\]', '', response)

        wiki_embed = discord.Embed(color=discord.Color.green())
        wiki_embed.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)
        wiki_embed.add_field(name=busqueda, value=response_clean)
        wiki_embed.add_field(name="Enlace al artículo:", value=the_url, inline=False)
        wiki_embed.set_footer(text="Extraído de Wikipedia", icon_url="https://cdn.icon-icons.com/icons2/2699/PNG/512/wikipedia_logo_icon_168863.png")
        await ctx.respond(embed=wiki_embed)

def setup(client):
    client.add_cog(Wikipedia_API(client))