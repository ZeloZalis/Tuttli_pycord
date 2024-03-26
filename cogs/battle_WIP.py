import json
import random
import discord
from discord.ext import commands

class Battle_start():
    def __init__(self, user1, user2, thread_id):
        self.user1 = user1
        self.user1_hp = 100
        self.user1_turn = None
        self.user2 = user2
        self.user2_hp = 100
        self.thread_id = thread_id
    
    def Victory_Lose(self):
        if self.user1_hp <= 0:
            #Ha ganado el jugador 1
            pass
        elif self.user2_hp <= 0:
            #Ha ganado el jugador 2
            pass
        else:
            #Se repite la fase de combate
            self.Battle_phase()
    def First_turn(self):
        num = 10
        #Se consigue un numero al azar
        if num%2 == 0:
            self.user1_turn = True
        else:
            self.user1_turn = False
    def Battle_phase(self):
        if self.user1_turn == True:
            #Acá se mandará un embed con un botón para escojer la acción
            #En principio sólo se podrá usar ataque
            
            #De esta manera cambiamos el turno al otro jugador
            self.user1_turn == False
            self.Victory_Lose()
            pass
        elif self.user1_turn == False:
            #Lo mismo, pero para el jugador dos
            self.user1_turn == True
            self.Victory_Lose()
            pass
class Combat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids=[522277286024708096, 574449304832311297], name="duel", description="Retas a un usuario a un combate.")
    async def duel(self, ctx, member:discord.Member):
        await ctx.defer()
        channel_used = ctx.channel

        if member is None:
            print("El jugador no está en el servidor.")
            await ctx.respond("El jugador no se encuentra en este servidor.")

        else:
            await ctx.respond(f"Reto enviado a {member.display_name}.")
            print("Se ha entrado en el else.")
            channel = ctx.channel
            print(f"Canal obtenido: {channel}")

            class MyView(discord.ui.View):
                def __init__(self):
                    super().__init__()
                    self.used = False

                print("Clase creada")
                used = False
                @discord.ui.select(
                    placeholder="¿Aceptas el reto?",
                    max_values=1,
                    options=[
                        discord.SelectOption(label="Sí", value="1", emoji="⭕"),
                        discord.SelectOption(label="No", value="0", emoji="❌")
                    ])
                
                async def callback(self, select, interaction):
                    print("Callback creado.")
                    if self.used:
                        await member.send("Ya has respondido al duelo.")
                        return
                    
                    if select.values[0] == "1":
                        print("Valor obtenido: yes")
                        message = await channel_used.send(f"Ha iniciado el combate entre {ctx.author.mention} y {member.mention}.")
                        battle_thread = await channel_used.create_thread(name="Combate por turnos", message=message, type=discord.ChannelType.public_thread)
                        print("thread creado.")
                        print("Mensaje enviado en el thread.")
                        await interaction.response.send_message(f"Has aceptado el duelo, la contienda se realizará en: {battle_thread.mention}.")
                        self.used = True

                    elif select.values[0] == "0":
                        print("Valor obtenido: no")
                        await interaction.response.send_message("Se ha cancelado el combate.")
                        await channel_used.send("El usuario ha rechazado el duelo.")
                        print("Respuesta negativa enviada al canal.")
                        self.used = True

            view = MyView()
            print("View creado.")
            await member.send(f"{ctx.author.mention} te ha retado a un duelo.", view=view)
            print("Mensaje de reto enviado.")

def setup(client):
    client.add_cog(Combat(client))