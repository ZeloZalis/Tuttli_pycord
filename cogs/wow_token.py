import discord
import requests
import datetime
from decouple import config
from discord.ext import commands

eng_to_esp = {
    "days" : {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    },
    "months":{
        'January': 'enero',
        'February': 'febrero',
        'March': 'marzo',
        'April': 'abril',
        'May': 'mayo',
        'June': 'junio',
        'July': 'julio',
        'August': 'agosto',
        'September': 'septiembre',
        'October': 'octubre',
        'November': 'noviembre',
        'December': 'diciembre'
    }
}

def create_access_token(client_id, client_secret, region="us"):
    data = {'grant_type': 'client_credentials'}
    response = requests.post(
        'https://%s.battle.net/oauth/token' % region,
        data=data,
        auth=(client_id, client_secret)
    )
    return response.json()

class WoW_Token(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="wow_token", description="Muestra el precio del Token de WoW en America y Europa.")
    async def Wow_token(self, ctx):
        await ctx.defer()
        try:
            token = create_access_token(config("wow_client_id"), config("wow_client_secret"))
            dataUS = requests.get(f"https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US&access_token={token['access_token']}")
            infoUS = dataUS.json()
            dataEU = requests.get(f"https://eu.api.blizzard.com/data/wow/token/index?namespace=dynamic-eu&locale=en_US&access_token={token['access_token']}")
            infoEU = dataEU.json()
            timestamp = infoUS['last_updated_timestamp'] / 1000
            date = datetime.datetime.fromtimestamp(timestamp)
            date_modified_1 = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            date_modified_2 = date_modified_1.strftime('%A, %d de %B de %Y, %I:%M:%S %p')
            for eng, esp in eng_to_esp["days"].items():
                date_modified_2 = date_modified_2.replace(eng, esp)
            for eng, esp in eng_to_esp["months"].items():
                date_modified_2 = date_modified_2.replace(eng, esp)
            date_modified_2 = date_modified_2.replace('AM', 'a.m.').replace('PM', 'p.m.') #Palabra exacta

            token_embed = discord.Embed(title="World of Warcraft Token", description="", color=discord.Color.random())
            token_embed.add_field(name="AMERICAS", value=f"{infoUS['price']/10**7}g")
            token_embed.add_field(name="EUROPA", value=f"{infoEU['price']/10**7}g")
            token_embed.set_footer(
                text=date_modified_2,
                icon_url="https://cdn.discordapp.com/avatars/1186161512298074122/099fc4f5836e1152d3625345eae7f1ad.png"
            )
            token_embed.set_image(url="https://static.wikia.nocookie.net/wowpedia/images/0/05/WoW_Token_Shop.jpg")
            await ctx.followup.send(embed=token_embed)
        except Exception as e:
            print(f"Ha ocurrido un error con el comando Wow_token: {e}")
            await ctx.respond("Ha ocurrido un error.")

def setup(client):
    client.add_cog(WoW_Token(client))