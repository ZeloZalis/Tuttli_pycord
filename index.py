import os
import json
import discord
from discord import Game
from decouple import config
from datetime import datetime

#Inicializamos el bot en una variable
client = discord.Bot()
intents = discord.Intents.default()
intents.messages = True

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

#La siguiente función sirve para recoger el día, mes y año
#Y lo guarda en una variable concatenando los datos en una sola
#Cadena, .zfill(2) se utiliza para asegurarse de que cada valor
#Tenga mínimo 2 caracteres
def Get_datetime():
    today = datetime.now()
    today_info = str(today.day).zfill(2) + str(today.month).zfill(2) + str(today.year)
    return today_info

#before_invoke se utiliza para invocar una función delante de otra de manera automática
#En este caso, la función recoge los datos del autor, del servidor y del comando que
#Se está ejecutando para imprimirlo en pantalla a manera de log
@client.before_invoke
async def Get_logs(ctx):
    date_time = Get_datetime()
    log = {
        "author_name": ctx.author.name,
        "author_id": ctx.author.id,
        "guild_name": ctx.guild.name,
        "guild_id": ctx.guild.id,
        "command_used": client.get_command(ctx.command.name).name
    }
    with open(f"./local/CommandLogs{date_time}.txt", "a+") as f:
        json.dump(log, f)
    print(f"El usuario {log['author_name']} ({log['author_id']}) ha ejecutado el comando {log['command_used']} en {log['guild_name']} ({log['guild_id']}).")

#Este es un comando global (no necesita agregar los servidores en los que funcionará)
#Al ser comando global, tarda en actualizarse en todos los servidores
@client.slash_command(name="ping", description="Muestra el ping del bot.")
async def Ping(ctx):
    await ctx.respond(f"Mi ping es de {int(client.latency*1000)} ms.")

#La siguiente línea de comando, detecta un mensaje en channel_id, y si el mensaje
#Contiene un Embed, lo copia y lo envía en thread_id
    # message.author.bot
@client.event
async def on_message(message):
    if message.type != discord.MessageType.default:
        return
    channel_id = 1166507853314539561
    thread_id = 1206075832016175155

    if message.channel.id == channel_id:
        if message.embeds:
            print(f"Mensaje detectado en {channel_id}.")
            guild = message.guild
            thread = guild.get_thread(thread_id)
            if thread:
                print(f"Mensaje incrustado en el hilo {thread_id}.")
                embed = message.embeds[0]
                await thread.send(embed=embed) 
            else:
                print("Error, no se ha enviado el mensaje.")
        else:
            print("El mensaje del canal no contiene un embed.")

client.run(config("token"))