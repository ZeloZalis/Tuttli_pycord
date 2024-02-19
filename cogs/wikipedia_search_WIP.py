import re
import discord
import requests
import wikipedia
from bs4 import BeautifulSoup
from discord.ext import commands

#Declaramos el lenguaje en el que trabajará wikipedia
#En este caso, Español
wikipedia.set_lang("es")

testing_server = [522277286024708096, 574449304832311297]

class SelectMenu(discord.ui.Select):
    def __init__(self, cog, des_options):
        self.cog = cog
        fix_options = list(dict.fromkeys(des_options))
        options = [discord.SelectOption(label=i) for i in fix_options[1:]]
        super().__init__(placeholder="Selecciona una opción", options=options)
    
    async def callback(self, interaction: discord.Interaction):
        response = wikipedia.summary(self.values[0], sentences=2)
        parrafo = {
            'action':'query',
            'format':'json',
            'titles':self.values[0],
            'prop':'info',
            'origin':'*'
        }
        request_api = requests.get("https://es.wikipedia.org/w/api.php", params=parrafo)
        data = request_api.json()
        first_page = next(iter(data['query']['pages'].values()))
        the_url = f"https://es.wikipedia.org/?curid={first_page['pageid']}"
        lis = BeautifulSoup(the_url, features="html.parser").find_all('li')
        response_clean = re.sub(r'\[\d+\]|\[\d+\]\[.*?\]|\[http.*?\]', '', response)

        wiki_embed = discord.Embed(color=discord.Color.green())
        wiki_embed.set_author(name=f"Pedido por: {self.cog.ctx.author.name}", icon_url=self.cog.ctx.author.avatar)
        wiki_embed.add_field(name=self.values[0].upper(), value=response_clean)
        wiki_embed.add_field(name="Enlace al artículo:", value=the_url, inline=False)
        wiki_embed.set_footer(text="Extraído de Wikipedia", icon_url="https://cdn.icon-icons.com/icons2/2699/PNG/512/wikipedia_logo_icon_168863.png")
        await interaction.response.send_message(embed=wiki_embed)

class Desambiguation(discord.ui.View):
    def __init__(self, cog, des_options):
        super().__init__()
        self.add_item(SelectMenu(cog, des_options))

class Wikipedia_API(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ctx = None
        self.busqueda_up = None

    @commands.slash_command(guild_ids = testing_server, name='wiki', description="Para buscar algo en wikipedia.")
    async def wiki(self, ctx, *, busqueda: str):
        self.ctx = ctx
        self.busqueda_up = busqueda.upper()
        #El defer() se utiliza para notificar a la API
        #Que el comando que se realizará tomará tiempo en
        #Realizarse, debido a que la API por defecto tiene
        #Un tiempo de espera máximo de 3 segundos, si la acción
        #No se realiza en los 3 segundos, dará error, cosa que se puede evitar con un defer()
        await ctx.defer()
        # busqueda_up = busqueda.upper()

        try:
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

        
            #Ahora, realizamos la búsqueda, y ponemos un límite de 2 párrafos
            response = wikipedia.summary(busqueda, sentences=2)
            #El re.sub es para eliminar ciertos caracteres de la respuesta
            response_clean = re.sub(r'\[\d+\]|\[\d+\]\[.*?\]|\[http.*?\]', '', response)

            #Creamos un Embed que contendrá la información de la búsqueda para imprimirlo en un mensaje
            wiki_embed = discord.Embed(color=discord.Color.green())
            wiki_embed.set_author(name=f"Pedido por: {ctx.author.name}", icon_url=ctx.author.avatar)
            wiki_embed.add_field(name=self.busqueda_up, value=response_clean, inline=False)
            wiki_embed.add_field(name="Enlace al artículo:", value=the_url, inline=False)
            wiki_embed.set_footer(text="Extraído de Wikipedia", icon_url="https://cdn.icon-icons.com/icons2/2699/PNG/512/wikipedia_logo_icon_168863.png")
            await ctx.respond(embed=wiki_embed)
    
        #La siguiente excepción es para guardar el error de búsqueda
        #Cuando haya más de 1 resultado posible, y mostrarlo por pantalla
        #Para que el usuario decida cuál resultado quiere
        except wikipedia.DisambiguationError as e:
            view = Desambiguation(self, e.options)
            await ctx.respond("Selecciona una opción.", view=view, ephemeral=True)

def setup(client):
    client.add_cog(Wikipedia_API(client))