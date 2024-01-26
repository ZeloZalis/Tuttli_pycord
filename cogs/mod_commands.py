import discord
from discord import Option
from discord.ext import commands

client = discord.Bot()
testing_server = [522277286024708096, 574449304832311297]

#Los siguientes comandos son comandos de moderación que sólo podrán ser usados
#Por el staff del servidor

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    #El siguiente comando sirve para kickear a un usuario del servidor, tomando
    #Los siguientes valores: usuario y motivo del kick

    @client.slash_command(guild_ids=testing_server, name="kick", description="Kickea un miembro del server.")
    @commands.has_permissions(kick_members=True)
    @commands.has_role("Mod")
    async def Kick(self, ctx, member: discord.Member, *, modreason: str):
        await member.kick(reason=modreason)
        kick_embed = discord.Embed(
            title="A casa platita.",
            description=f"{member.mention} ha sido papiado por {ctx.author.mention}.",
            color=discord.Color.green()
            )
        kick_embed.add_field(name="Motivo:", value=modreason, inline=False)
        kick_embed.set_image(url="https://c.tenor.com/TG5OF7UkLasAAAAC/tenor.gif")
        await ctx.respond(embed=kick_embed)
    
    #El siguiente comando sirve para banear a un usuario del servidor, tomando
    #Los siguientes valores: usuario y motivo del ban

    @client.slash_command(guild_ids = testing_server, name = "ban", description = "Banea un miembro del server.")
    @commands.has_permissions(ban_members = True, administrator = True)
    @commands.has_role("Mod")
    async def Ban(
        self, ctx,
        member: Option(discord.Member, description = "¿A quién quieres banear?"),
        modreason: Option(str, description = "Motivo del baneo.", required = True)
        ):
        ban_embed = discord.Embed(
            title="A casa platita.",
            description=f"{member.mention} ha sido evangelizado por {ctx.author.mention}.",
            color=discord.color.green()
            )
        ban_embed.add_field(name="Motivo:", value=modreason, inline=False)
        ban_embed.set_image(url="https://c.tenor.com/TG5OF7UkLasAAAAC/tenor.gif")
        await member.ban(reason=modreason)
        await ctx.respond(embed=ban_embed)







    # @client.slash_command(guild_ids=testing_server, name="ban", description="Banea un miembro del server.")
    # @commands.has_permissions(ban_members=True)
    # @commands.has_role("Mod")
    # async def ban(self, ctx, member: discord.Member, *, modreason: str):
    #     await member.ban(reason=modreason)

    #     conf_embed = discord.Embed(title="A casa platita.", description=f"{member.mention} ha sido evangelizado por {ctx.author.mention}.", color=discord.color.green())
    #     conf_embed.add_field(name="Motivo:", value=modreason, inline=False)
    #     conf_embed.set_image(url="https://c.tenor.com/TG5OF7UkLasAAAAC/tenor.gif")
    #     await ctx.respond(embed=conf_embed)





    #El siguiente comando es para quitarle ban a un usuario
    #En este caso, como no se puede etiquetar al usuario, se requiere ingresar el ID del mismo

    @client.slash_command(guild_ids=testing_server, name="unban", description="Desbanea un miembro del server.")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.has_role("Mod")
    async def unban(self, ctx, userid):
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)
        
        confirmation_embed = discord.Embed(title="Exitoso.", color=discord.color.green())
        confirmation_embed.add_field(name="Desbaneado:", value=f"<@{userid}> ha sido desbaneado del server por {ctx.author.mention}", inline=False)
        await ctx.send(embed=confirmation_embed)


def setup(client):
    client.add_cog(Moderation(client))