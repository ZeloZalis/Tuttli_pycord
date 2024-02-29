import discord
from datetime import date
from discord.ext import commands

servers = [522277286024708096]

class TrainingRoutine(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(guild_ids=servers, name="fitness", description="Muestra una rutina de ejercicios personalizada.")
    @commands.has_role("Shōgun")
    async def fitness(self, ctx):
        today = date.today()
        day = today.weekday()
        if day == 0:
            fitness_embed = discord.Embed(title="Rutina Lunes", description="Pecho y tríceps", color=discord.Color.random())
            fitness_embed.add_field(name="Press de banca con mancuernas", value="4 Series de 10 Repeticiones.")
            fitness_embed.add_field(name="Aperturas con mancuernas", value="3 Series de 12 Repeticiones.")
            fitness_embed.add_field(name="Fondos en banca", value="3 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Extensiones de tríceps con mancuerna", value="3 Series de 12 Repeticiones por brazo.")
            fitness_embed.add_field(name="Patada de tríceps con mancuerna", value="3 Series de 15 Repeticiones por brazo.")
            await ctx.respond("Aquí tienes la rutina de hoy.", embed=fitness_embed)
        elif day == 1:
            fitness_embed = discord.Embed(title="Rutina Martes", description="Espalda y bíceps", color=discord.Color.random())
            fitness_embed.add_field(name="Remo con mancuerna", value="4 Series de 10 Repeticiones por brazo.")
            fitness_embed.add_field(name="Remo al mentón con mancuernas", value="3 Series de 12 Repeticiones.")
            fitness_embed.add_field(name="Pullover con mancuerna", value="3 Series de 12 Repeticiones.")
            fitness_embed.add_field(name="Curl de bíceps con mancuernas", value="3 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Curl de bíceps martillo con mancuernas", value="3 Series de 12 Repeticiones.")
            await ctx.respond("Aquí tienes la rutina de hoy.", embed=fitness_embed)
        elif day == 2:
            fitness_embed = discord.Embed(title="Rutina Miércoles", description="Piernas y glúteos", color=discord.Color.random())
            fitness_embed.add_field(name="Sentadillas con mancuernas", value="4 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Zancadas con mancuernas", value="3 Series de 12 Repeticiones por pierna.")
            fitness_embed.add_field(name="Peso muerto rumano con mancuernas", value="3 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Elevación de cadera con mancuerna", value="3 Series de 20 Repeticiones.")
            fitness_embed.add_field(name="Elevación de talones con mancuernas", value="3 Series de 25 Repeticiones.")
            await ctx.respond("Ya vas a la mitad, sigue así.", embed=fitness_embed)
        elif day == 3:
            fitness_embed = discord.Embed(title="Rutina Jueves", description="Hombros y abdominales", color=discord.Color.random())
            fitness_embed.add_field(name="Press militar con mancuernas", value="4 Series de 10 Repeticiones.")
            fitness_embed.add_field(name="Elevaciones laterales con mancuernas", value="3 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Elevaciones frontales con mancuernas", value="3 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Encogimientos de hombros con mancuernas", value="3 Series de 20 Repeticiones.")
            fitness_embed.add_field(name="Crunches", value="3 Series de 25 Repeticiones.")
            fitness_embed.add_field(name="Plancha", value="3 Series de 30 segundos.")
            await ctx.respond("Estás a un día de terminar.", embed=fitness_embed)
        elif day == 4:
            fitness_embed = discord.Embed(title="Rutina Viernes", description="Cuerpo completo", color=discord.Color.random())
            fitness_embed.add_field(name="Burpees con mancuernas", value="4 Series de 10 Repeticiones.")
            fitness_embed.add_field(name="Swing con mancuerna", value="4 Series de 15 Repeticiones.")
            fitness_embed.add_field(name="Thrusters con mancuernas", value="4 Series de 12 Repeticiones.")
            fitness_embed.add_field(name="Renegade row con mancuernas", value="4 Series de 10 Repeticiones por brazo.")
            fitness_embed.add_field(name="Mountain climbers", value="4 Series de 20 Repeticiones por pierna.")
            await ctx.respond("Con esto finalizamos la semana, a descansar!", embed=fitness_embed)

def setup(client):
    client.add_cog(TrainingRoutine(client))