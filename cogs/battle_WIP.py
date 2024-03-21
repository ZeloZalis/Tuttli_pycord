import json
import random
import discord
from discord.ext import commands

class Combat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids=[522277286024708096, 574449304832311297], name="challenge", description="Retas a un usuario a un combate.")
    async def challenge(self, ctx, member:discord.Member):
        await ctx.defer()
        if member is None:
            print("El jugador no está en el servidor.")
            await ctx.respond("El jugador no se encuentra en este servidor.")
        else:
            print("Se ha entrado en el else.")
            channel = ctx.channel
            print(f"Canal obtenido: {channel}")
            class MyView(discord.ui.View):
                print("Clase creada")
                @discord.ui.select(
                    placeholder=f"{ctx.author.name} Te han retado a un duelo, ¿aceptas?",
                    options=[
                        discord.SelectOption(label="Sí", value="yes", emoji="⭕"),
                        discord.SelectOption(label="No", value="no", emoji="❌")
                    ])
                async def callback(self, select):
                    print("Callback creado.")
                    if select.values[0] == "yes":
                        print("Valor obtenido: yes")
                        battle_thread = await channel.create_thread(name="Hilo de combate")
                        print("thread creado.")
                        await battle_thread.send("Que comience el combate.")
                        print("Mensaje enviado en el thread.")
                    elif select.values[0] == "no":
                        print("Valor obtenido: no")
                        await ctx.send("Se ha cancelado el combate.")
                        print("Respuesta negativa enviada al retado.")
            view = MyView()
            print("View creado.")
            await member.send("Escoge una opción", view=view)
            print("Mensaje de reto enviado.")
    @commands.slash_command(guild_ids=[522277286024708096, 574449304832311297], name="thread", description="crea un thread")
    async def tread(self, ctx):
        try:
            message = await ctx.channel.send(f"Ha iniciado el combate entre {ctx.author.mention} y USER_2")
            hilo = await ctx.channel.create_thread(name="Combate por turnos.", message=message, type=discord.ChannelType.public_thread)
            user1_id = ctx.author.id
            user2_id = 1235
            await ctx.respond("Se ha creado el thread.", ephemeral=True)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            # await hilo.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            overwrite_invite = discord.PermissionOverwrite()
            overwrite_invite.send_messages = True
            overwrite_invite.read_messages = True
            # await hilo.set_permissions(user1_id, overwrite=overwrite_invite)
            # await hilo.set_permissions(user2_id, overwrite=overwrite_invite)
        except Exception as e:
            print(f"Se ha producido un error: {e}.")
            await ctx.respond(f"Se ha producido un error: {e}.")

def setup(client):
    client.add_cog(Combat(client))