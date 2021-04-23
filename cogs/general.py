import discord
from discord.ext import commands
from discord.ext.commands import Cog
import os
import json
config = os.path.abspath('./config.json')
with open(str(config),"r") as cfg:
    cont = cfg.read()
    jso = json.loads(cont)
    prefix = jso["prefix"]
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")
class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        print("General cog loaded!")
    # Info command.
    @commands.command(name="info")
    async def info(self, ctx):
        embed=discord.Embed(title="Information")
        embed.add_field(name="What is DingDong?",value="DingDong is a multi-purpose Discord bot. It has moderation features as well as more fun ones, though the fun ones will be moved to a separate bot in the future.",inline=False)
        embed.add_field(name="Author:",value="<@207358306451193857>",inline=False)
        embed.add_field(name="Created on:",value="September 4, 2020",inline=False)
        await ctx.send(embed=embed)
    @commands.command(name="cmds")
    async def cmds(self, ctx, page):
        # Checks arguments. For example: This one checks moderation
        if page.lower() == "moderation" or page.lower() == "mod":
            embed = discord.Embed(title="Moderation commands")
            embed.add_field(
                name="mute", value=f"Mute players. The reason is optional.\n{prefix}mute <member> <reason>")
            embed.add_field(
                name="unmute", value=f"Unmute players.\n{prefix}unmute <member>")
            embed.add_field(
                name="lock", value=f"Locks the channel, preventing speech in it.\n{prefix}lock")
            embed.add_field(
                name="unlock", value=f"Unlocks the channel, allowing speech in it.\n{prefix}unlock")
            await ctx.send(embed=embed)
        # This one checks fun
        elif page.lower() == "fun":
            embed = discord.Embed(title="Fun commands")
            embed.add_field(
                name="keyboard", value=f"Converts your text into different 'keyboards'.\n{prefix}keyboard [keyboard] [content]")
            embed.add_field(
                name="(r)eddit", value=f"Grabs random post from subreddit you specify. Blocks NSFW subreddits.\n{prefix}reddit [subreddit]"
            )
            await ctx.send(embed=embed)
        # And this one checks info.
        elif page.lower() == "info" or page.lower() == "information":
            embed = discord.Embed(title="Fun commands")
            embed.add_field(
                name="info", value=f"Posts general story and history of the bot.\n{prefix}info", inline=False
            )
            embed.add_field(
                name="cmds",value=f"Pulls up all commands for the bot.\n{prefix}cmds [section]"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="You seem to be stuck.")
            embed.add_field(name="Here are the valid pages you can go to.",
                            value="fun,(mod)eration,(info)rmation", inline=False)
            embed.set_footer(text="Case sensitive")
            await ctx.send(embed=embed)
    @cmds.error
    async def cmds_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="You seem to be stuck.")
            embed.add_field(name="Here are the valid pages you can go to.",
                            value="fun,(mod)eration,(info)rmation", inline=False)
            embed.set_footer(text="Case sensitive")
            await ctx.send(embed=embed)
            return
    # Message delete
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = await client.fetch_channel(713855953782702103)
        await channel.send(f"Someone tried to delete a message.\nAuthor: {message.author}\nMessage: {message.content}\nMessage created at: {message.created_at}\nChannel: #{message.channel}\nGuild: {message.guild}")
        if message.attachments != []:
            await channel.send(message.attachments[0].url)
    # Message edit
    @commands.Cog.listener()
    async def on_message_edit(self, message, nmessage):
        channel = await client.fetch_channel(713855953782702103)
        if message.edited_at == None:
            await channel.send(f"Someone tried to edit their message.\nAuthor: {message.author}\nOriginal message: {message.content}\nNew message: {nmessage.content}\nOriginal time: {message.created_at}\nTime of edit: No prior edits\nChannel: #{message.channel}\nGuild: {message.guild}")
            if message.attachments != []:
                await channel.send(message.attachments[0].url)
        else:
            await channel.send(f"Someone tried to edit their message.\nAuthor: {message.author}\nOriginal Message: {message.content}\nNew message: {nmessage.content}\nOriginal time: {message.created_at}\nTime of edit: {message.edited_at}\nChannel: #{message.channel}\nGuild: {message.guild}")
            if message.attachments != []:
                await channel.send(message.attachments[0].url)
def setup(client):
    client.add_cog(General(client))
