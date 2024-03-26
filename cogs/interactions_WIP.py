import json
import random
import discord
from discord.ext import commands

class Interactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="attack", description="Atacas a una persona.")
    async def attack(self, ctx, member: discord.Member):
        try:
            with open(f"resources/attack.txt", "r", encoding="utf-8") as file:
                response_list = [json.loads(line) for line in file.readlines()]
                response = random.choice(response_list)
            attack_embed = discord.Embed(color=discord.Color.random())
            # attack_embed.set_author(name=f"{ctx.author.display_name} {response['description']} {member.display_name}.", icon_url=ctx.author.avatar)
            attack_embed.set_image(url=f"{response['url']}")
            attack_embed.set_footer(text=f"Anime: {response['name']}")
            await ctx.respond(f"**{ctx.author.display_name}** {response['description']} {member.mention}.", embed=attack_embed)
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            await ctx.respond("Ha ocurrido un error.")
    
def setup(client):
    client.add_cog(Interactions(client))