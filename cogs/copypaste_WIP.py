# import discord
# from discord.ext import commands

# testing_server = [522277286024708096, 574449304832311297]

# class Message_copy(commands.Cog):
#     def __init__(self, client):
#         self.client = client

#     async def on_message(self, message):
#         if message.author.bot or message.type != discord.MessageType.default:
#             return
#         _id = 1166507853314539561
#         thread_id = 1206075832016175155

#         if message.channel.id == channel_id:
#             if message.embeds:
#                 guild = message.guild
#                 thread = guild.get_thread(thread_id)
#                 if thread:
#                     embed = message.embeds[0]
#                     await thread.send(embed=embed)
        
#         await self.process_commands(message)

# def setup(client):
#     client.add_cog(Message_copy(client))