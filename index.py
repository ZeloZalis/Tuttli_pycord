import os
import discord
from discord import Game
from decouple import config

#Inicializamos el bot en una variable
client = discord.Bot()

#Se ejecuta al iniciar el bot
#El change_presence es para cambiar el mensaje "jugando" del bot
@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="/help"))
    print(f"I just logged as {client.user}")

#Las siguientes líneas de código son para cargar los cogs
cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]
for cogfile in cogfiles:
    print(f"Intentando cargar {cogfile}")
    try:
        client.load_extension(cogfile)
    except Exception as e:
        print(f"Error: {e}")

#Variable con el ID de los servidores en los que
#Se está testeando el bot
testing_server = [522277286024708096, 574449304832311297]

#before_invoke se utiliza para invocar una función delante de otra de manera automática
#En este caso, la función recoge los datos del autor, del servidor y del comando que
#Se está ejecutando para imprimirlo en pantalla a manera de log
@client.before_invoke
async def Get_logs(ctx):
    author_id = ctx.author.id
    author_name = ctx.author.name
    guild_id = ctx.guild.id
    guild_name = ctx.guild.name
    command_name = client.get_command(ctx.command.name).name
    print(f"El usuario {author_name} ({author_id}) ha ejecutado el comando {command_name} en {guild_name} ({guild_id}).")

#Este es un comando global (no necesita agregar los servidores en los que funcionará)
#Al ser comando global, tarda en actualizarse en todos los servidores
@client.slash_command(name="ping", description="Muestra el ping del bot.")
async def Ping(ctx):
    await ctx.respond(f"Mi ping es de {int(client.latency*1000)} ms.")

client.run(config("token"))