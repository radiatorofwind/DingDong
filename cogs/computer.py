import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Cog
import os
import json
config = os.path.abspath('./config.json')
with open(str(config), "r") as cfg:
    cont = cfg.read()
    jso = json.loads(cont)
    prefix = jso["prefix"]
client = commands.Bot(command_prefix=prefix)
class Computer:
    # This is going to be very tough.
    # Let me lay down the structure for myself, though.
    # I'm creating a class called Computer as an attempt to group everything into different sections 
    # - Start command creates a new class called Computer with separate user ids and the screen id.
    # - The user ID prevents conflicts with other computer screens, while the screen ID is the ID of the screen
    # - The screen is just a message that is edited.
    # - I'll be honest, I think I'll just
    #
    #
    #
    #
    #
    def __init__(self, user_id):
        self.user_id = None
        self.already_on = True
    desktop = discord.Embed(title="Desktop")
    desktop.add_field(name="Choose what you want to do:",
                      value="🪐 Go online\n🎮 Play games\n🗒️ Open Notepad\n❌ Shut down the computer", inline=False)
    notepad = discord.Embed(title="Notepad")
    notepad.add_field(name="Start typing!",value="Everything you type from here on out is going to be saved in your notepad.\nSay 'stop notepad' to stop noting everything down.",inline=False)
    desktopemojis = ["🪐", "🎮", "🗒️", "❌"]
    x = "❌"
    current_screen = desktop
    notepad_on = False
    async def createscreen(self,channel_id):
        channel = await client.fetch_channel(channel_id)
        if not channel:
            raise(RuntimeError("The channel you tried to fetch wasn't found!"))
        await channel.send(embed=current_screen)
class DingDOS(commands.Cog):
    def __init__(self,client):
        self.client = client
        print("Computer cog loaded!")
        global current_users
        current_users = []
    @commands.command(name="start",description="Start up the computer. Creates the interface.")
    async def startpc(self, ctx):
        if ctx.author.id in current_users:
            await ctx.send("The computer is already turned on.")
        else:
            computerC = Computer(ctx.author.id)
            current_users.append(ctx.author.id)
            spinner = "|/-\\"
            global startup
            compscreen = await ctx.send("DingDOS is starting up...")
            for i in range(3):
                for s in spinner:
                    await compscreen.edit(content=f"DingDOS is starting up...\n{s}")
                    await asyncio.sleep(0.1)
            await compscreen.edit(content="",embed=computerC.current_screen)
            for emoji in computerC.desktopemojis:
                await compscreen.add_reaction(emoji)
def setup(client):
    client.add_cog(DingDOS(client))
