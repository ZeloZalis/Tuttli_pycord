import random
import discord
from discord.ext import commands

#1
##############################################################################
class SelectMenu(discord.ui.Select):
    def __init__(self, cog, atk_list):
        self.cog = cog
        self.attack_list = atk_list
        options = [
            discord.SelectOption(
                label= attack['name'],
                value= attack['name'],
                emoji= attack['type'],
                description= attack['description']
            ) for attack in self.attack_list
        
        ]
        super().__init__(placeholder="Selecciona un ataque", options=options)
    
    async def callback(self, interaction: discord.Interaction):


        await interaction.response.send_message(f"Callback.")
class Desambiguation(discord.ui.View):
    def __init__(self, cog, atk_list):
        super().__init__()
        self.add_item(SelectMenu(cog, atk_list))
##############################################################################

class Battle_start():
    def __init__(self, cog, retador, retado, thread_id):
        self.author = retador
        self.member = retado
        self.user1_hp = 100
        self.user1_turn = None
        self.user2_hp = 100
        self.thread_id = thread_id
        self.cog = cog
    
    async def Victory_Lose(self):
        if self.user1_hp <= 0:
            #Ha ganado el jugador 2
            pass
        elif self.user2_hp <= 0:
            #Ha ganado el jugador 1
            pass
        else:
            #Se repite la fase de combate
            self.Battle_phase()

    async def Switch_turn(self, turn):
        # print("Entró a la función de cambio de turno.")
        if turn == True:
            # print("Cambio de True a False.")
            self.user1_turn = False
            return
        elif turn == False:
            # print("Cambio de False a True.")
            self.user1_turn = True
            return
        else:
            # print(f"Valor de turno no válido: {turn}")
            return
    async def Battle_phase(self):
        # print("Entró en Battle_phase.")
        num = random.randint(1, 6)
        # print(f"Número obtenido: {num}")
        if num%2 == 0:
            self.user1_turn = True
            # print("Se entró en el número par.")
        else:
            self.user1_turn = False
            # print("Se entró en el número impar.")

        while True:
            # print("Inicia el ciclo")
            if self.user1_turn == True:
                # print("Se entró en el if True.")
                await self.thread_id.send(f"Turno de {self.author.display_name}.")
                # print("Mensaje enviado True.")
                with open("resources/battle/skills.txt", encoding="utf-8") as file:
                    read_lines = file.readlines()
                    attack_list = random.sample(read_lines, 3)
                    # print(f"{attack_list}")
                diccio = [eval(i) for i in attack_list]
                battle_view = Desambiguation(self, diccio)
                print("Se ha creado el view en la función de combate.")
                battle_view.add_item(SelectMenu(self.cog, diccio))
                print("Se ha llamado al view.")
                await self.thread_id.send(view=battle_view)
                break
                #Acá se mandará un embed con un botón para escojer la acción
                #En principio sólo se podrá usar ataque
            
                #De esta manera cambiamos el turno al otro jugador
                await self.Switch_turn(self.user1_turn)
                # await self.Victory_Lose()

            if self.user1_turn == False:
                # print("Se entró en el if False.")
                await self.thread_id.send(f"Turno de {self.member.display_name}.")
                # print("Mensaje enviado False")
                #Lo mismo, pero para el jugador dos
                with open("resources/battle/skills.txt", encoding="utf-8") as file:
                    read_lines = file.readlines()
                    attack_list = random.sample(read_lines, 3)
                    # print(f"{attack_list}")
                diccio = [eval(i) for i in attack_list]
                battle_view = Desambiguation(self, diccio)
                print("Se ha creado el view en la función de combate.")
                battle_view.add_item(SelectMenu(self.cog, diccio))
                print("Se ha llamado al view.")
                await self.thread_id.send(view=battle_view)
                break
                await self.Switch_turn(self.user1_turn)
                # await self.Victory_Lose()
    
    async def Surrender(self):
        if self.user1_turn == True:
            #Se rinde el jugador uno
            pass
        else:
            #Se rinde el jugador dos
            pass


class Combat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ctx = None

    #El siguiente comando será para retar a un jugador a un duelo, en el mismo se desarrollará todo
    @commands.slash_command(guild_ids=[522277286024708096, 574449304832311297], name="duel", description="Retas a un usuario a un combate.")
    async def duel(self, ctx, member:discord.Member):
        #Defer para esperar una respuesta (se debe agregar un tiempo máximo que se puede esperar para aceptar/rechazar)
        await ctx.defer()
        #Obtenemos el canal en una variable, y ctx también
        channel_used = ctx.channel
        self.ctx = ctx

        #Confirmamos primero si el miembro está en dicho servidor
        if member is None:
            # print("El jugador no está en el servidor.")
            await ctx.respond("El jugador no se encuentra en este servidor.")
        else:
            await ctx.respond(f"Reto enviado a {member.display_name}.")
            # print("Se ha entrado en el else.")
            channel = ctx.channel
            # print(f"Canal obtenido: {channel}")

            #Creamos el objeto que enviará la pregunta al usuario
            class MyView(discord.ui.View):
                def __init__(self):
                    super().__init__()
                    self.used = False

                # print("Clase creada")
                used = False
                @discord.ui.select(
                    placeholder="¿Aceptas el reto?",
                    max_values=1,
                    options=[
                        discord.SelectOption(label="Sí", value="1", emoji="⭕"),
                        discord.SelectOption(label="No", value="0", emoji="❌")
                    ])
                
                #El callback es lo que se realizará dependiendo de si acepta o no el reto
                async def callback(self, select, interaction):
                    print("Callback creado.")
                    #La siguiente condicional es para que no pueda responder más de una vez
                    if self.used:
                        await member.send("Ya has respondido al duelo.")
                        return
                    
                    #Esta condicional es para cuando el jugador acepte el duelo
                    if select.values[0] == "1":
                        #Se crea un mensaje de inicio y se crea el thread para el combate
                        message = await channel_used.send(f"Ha iniciado el combate entre {ctx.author.mention} y {member.mention}.")
                        battle_thread = await channel_used.create_thread(name="Combate por turnos", message=message, type=discord.ChannelType.public_thread)
                        
                        #Este es un mensaje de vuelta para el jugador retado
                        await interaction.response.send_message(f"Has aceptado el duelo, la contienda se realizará en: {battle_thread.mention}.")
                        self.used = True
                        
                        #Ahora se inicia la clase que maneja el combate
                        battle = Battle_start(self, ctx.author, member, battle_thread)
                        await battle.Battle_phase()
                    #Esta, para cuando lo rechaze
                    elif select.values[0] == "0":
                        # print("Valor obtenido: no")
                        await interaction.response.send_message("Se ha cancelado el combate.")
                        await channel_used.send("El usuario ha rechazado el duelo.")
                        # print("Respuesta negativa enviada al canal.")
                        self.used = True

            view = MyView()
            # print("View creado.")
            await member.send(f"{ctx.author.mention} te ha retado a un duelo.", view=view)
            # print("Mensaje de reto enviado.")

def setup(client):
    client.add_cog(Combat(client))