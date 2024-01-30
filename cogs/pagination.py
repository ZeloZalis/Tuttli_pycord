from discord.ext import commands
import discord

testing_server = [522277286024708096, 574449304832311297]

class PaginationView(discord.ui.View):
    current_page:int = 1
    sep:int = 5
    async def send(self, ctx):
        self.message = await ctx.send(view=self)
        await self.update_message(self.data[:self.sep])
    
    def create_embed(self, data):
        embed = discord.Embed(title=f"User List Page {self.current_page} / {int(len(self.data) / self.sep) + 1}")
        for item in data:
            embed.add_field(name=item["label"], value=item[""], inline=False)
        return embed

    async def update_message(self, data):
        self.update_buttons()
        await self.message.edit(embed=self.create_embed(data), view=self)
    
    def update_buttons(self):
        if self.current_page == 1:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == int(len(self.data) / self.sep) + 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary
    
    @discord.ui.button(label="First", style=discord.ButtonStyle.primary)
    async def First_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page = 1
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        await self.update_message(self.data[:until_item])

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
    async def Next_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page +=1
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        await self.update_message(self.data[from_item:until_item])

    @discord.ui.button(label="Back", style=discord.ButtonStyle.primary)
    async def Back_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page -=1
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        await self.update_message(self.data[from_item:until_item])

    @discord.ui.button(label="Last", style=discord.ButtonStyle.primary)
    async def Last_button(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_page = int(len(self.data) / self.sep) +1
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        await self.update_message(self.data[from_item:])
    
class Pagina(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(guild_ids=testing_server, name="pagination", description="Invoca una paginación.")
    async def pageinfo(self, ctx):
        data = range(1, 16)
        pagination_view = PaginationView()
        pagination_view.data = data
        await ctx.respond(pagination_view)


def setup(client):
    client.add_cog(Pagina(client))