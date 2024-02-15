import re
import discord
import requests
import wikipedia
from discord.ext import commands

#Declaramos el lenguaje en el que trabajará wikipedia
#En este caso, Español
wikipedia.set_lang("es")

testing_server = [522277286024708096, 574449304832311297]

class Wikipedia_API(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids = testing_server, name='wiki', description="Para buscar algo en wikipedia.")
    async def wiki(self, ctx, *, busqueda: str):
        #El defer() se utiliza para notificar a la API
        #Que el comando que se realizará tomará tiempo en
        #Realizarse, debido a que la API por defecto tiene
        #Un tiempo de espera máximo de 3 segundos, si la acción
        #No se realiza en los 3 segundos, dará error, cosa que se puede evitar con un defer()
        await ctx.defer()
        page_url = False
        busqueda_up = busqueda.upper()

        #El siguiente try es para conseguir el link de la página
        #Del contenido, si no se consigue obtener el enlace
        #No se mostrará en el Embed
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
            page_url = True

        
            #Ahora, realizamos la búsqueda, y ponemos un límite de 2 párrafos
            response = wikipedia.summary(busqueda, sentences=2)
            #El re.sub es para eliminar ciertos caracteres de la respuesta
            response_clean = re.sub(r'\[\d+\]|\[\d+\]\[.*?\]|\[http.*?\]', '', response)

            #Creamos un Embed que contendrá la información de la búsqueda para imprimirlo en un mensaje
            wiki_embed = discord.Embed(color=discord.Color.green())
            wiki_embed.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)
            wiki_embed.add_field(name=busqueda_up, value=response_clean)
            if page_url == True:
                wiki_embed.add_field(name="Enlace al artículo:", value=the_url, inline=False)
            wiki_embed.set_footer(text="Extraído de Wikipedia", icon_url="https://cdn.icon-icons.com/icons2/2699/PNG/512/wikipedia_logo_icon_168863.png")
            await ctx.respond(embed=wiki_embed)
    
        #La siguiente excepción es para guardar el error de búsqueda
        #Cuando haya más de 1 resultado posible, y mostrarlo por pantalla
        #Para que el usuario decida cuál resultado quiere
        except wikipedia.DisambiguationError as e:
            get_options = e.options
            class OptionList(discord.ui.View):
                def __init__(self):
                    super().__init__()

                @discord.ui.select(
                        placeholder="Opciones",
                        max_values=1,
                        min_values=1,
                        options=[discord.SelectOption(label=option, value=option.lower()) for option in get_options]
                )
                async def callback(self, select:discord.ui.Select, interaction: discord.Interaction):
                    print("Se ha iniciado el callback.")
                    await interaction.response.send_message(f"Has seleccionado {select.values[0]}")
            view = OptionList()
            print("View creado.")
            await ctx.respond(f"La palabra que estás buscando es algo ambigüa, he encontrado las siguientes opciones, escoge cuál es la que buscas.", view=view)
            print("Mensaje enviado en el chat.")
            # options = e.options #Devuelve ["Uno", "Dos"]

            # option_list = []
            # for i in options:
            #     option_list.append(f"{discord.SelectOption(label=options[i])}")
            # print(str(option_list))
            # class Option_list(discord.ui.View):
            #     @discord.ui.select(placeholder="Opciones", options=option_list)

                

            # message = f"'{busqueda}' puede referirse a:\n" + "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
            # await ctx.followup.send(f"Tienes las siguientes opciones: {options}")
            #Luego se agrega una lógica acá
        #El followup sirve para enviar más de un mensaje en respuesta a una interacción
        # await ctx.followup.send("Texto de prueba.")

def setup(client):
    client.add_cog(Wikipedia_API(client))