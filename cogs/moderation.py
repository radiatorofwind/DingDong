import discord
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
class DiscordModdery(commands.Cog):
    def __init__(self,client):
        self.client = client
        print("Moderation cog loaded!")
    @commands.command(name="lock")
    @commands.has_guild_permissions(administrator=True)
    async def lock(ctx):
        channel = client.get_channel(787804322637152256)
        if ctx.channel == channel:
            await ctx.send("You can't lock this channel.")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
            await ctx.send("Channel locked.")
    # unlock command
    @commands.command(name="unlock")
    @commands.has_guild_permissions(administrator=True)
    async def unlock(ctx):
        channel = client.get_channel(787804322637152256)
        if ctx.channel == channel:
            await ctx.send("You can't unlock this channel.")
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, add_reactions=True)
            await ctx.send("Channel unlocked.")
    @lock.error
    async def lock_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            return
    @unlock.error
    async def unlock_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            return
    @commands.command(name="mute")
    @commands.has_guild_permissions(administrator=True)
    async def mute(ctx, member: discord.Member, *reas):
        guil = client.get_guild(704902221153697833)
        if ctx.message.guild == guil:
            role = discord.utils.get(member.guild.roles, id=760544843276746823)
            reason = ' '.join(reas)
            if reason == '' or reason == []:
                await member.add_roles(role)
                await ctx.send(f"{member.mention} has been muted.")
            else:
                await member.add_roles(role, reason=reason)
                await ctx.send(f"{member.mention} has been muted for *{reason}*.")
        else:
            return
    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            return
    @commands.command(name="unmute")
    @commands.has_guild_permissions(administrator=True)
    async def unmute(ctx, member: discord.Member, *reas):
        guil = client.get_guild(704902221153697833)
        if ctx.message.guild == guil:
            role = discord.utils.get(member.guild.roles, id=760544843276746823)
            reason = ' '.join(reas)
            if reason == '' or reason == []:
                await member.remove_roles(role)
                await ctx.send(f"{member.mention} has been unmuted.")
            else:
                await member.remove_roles(role, reason=reason)
                await ctx.send(f"{member.mention} has been unmuted for *{reason}*.")
        else:
            return
    @unmute.error
    async def unmute_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            return
def setup(client):
    client.add_cog(DiscordModdery(client))
