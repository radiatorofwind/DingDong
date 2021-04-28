# dingdong.py
import discord
from discord.errors import HTTPException
from discord.ext import commands
from discord.ext.commands import Cog
import json
import time
import datetime
from datetime import datetime
# Take prefix and token from file
with open("config.json","r") as f:
    cntnt = f.read()
    jsn = json.loads(cntnt)
    token = jsn["token"]
    prefix = jsn["prefix"]
client = commands.Bot(command_prefix=prefix)
intents = discord.Intents.default()
intents.members = True
edgy = {"A":"Ä","a":"ą","B":"ß","b":"þ","C":"Ç","c":"ç","D":"Ð","d":"ď","E":"Ę","e":"ę","F":"Ƒ","f":"ƒ","G":"Ģ","g":"ģ","H":"Ħ","h":"ħ","I":"Ĩ","i":"ĭ","J":"ĵ","j":"Ĵ","K":"Ķ","k":"ĸ","L":"Ľ","l":"ľ","M":"Ṁ","m":"ṁ","N":"Ň","n":"ŋ","O":"Œ","o":"œ","P":"Ƥ","p":"ƥ","Q":"Ɋ","q":"ɋ","R":"Ɍ","r":"ɍ","S":"Ṡ","s":"ṡ","T":"Ŧ","t":"ŧ","U":"Ü","u":"ü","V":"V̄","v":"v̄","W":"Ŵ","w":"ŵ","X":"X̱","x":"x̱","Y":"Ƴ","y":"ƴ","Z":"Ƶ","z":"ƶ"," ":" ","@":"@","?":"¿",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"!","(":"(",")":")",",":",","\n":"\n"}
owospeak = {"A":"A","a":"a","B":"B","b":"b","C":"C","c":"c","D":"D","d":"d","E":"E","e":"e","F":"F","f":"f","G":"G","g":"g","H":"H","h":"h","I":"I","i":"i","J":"J","j":"j","K":"K","k":"k","L":"W","l":"w","M":"M","m":"m","N":"N","n":"n","O":"O","o":"o","P":"P","p":"p","Q":"Q","q":"q","R":"W","r":"w","S":"S","s":"s","T":"T","t":"t","U":"U","u":"u","V":"V","v":"v","W":"W","w":"w","X":"X","x":"x","Y":"Y","y":"y","Z":"Z","z":"z","th":"ff","Th":"Ff","TH":"FF","ove":"uv","Ove":"Uv","OVE":"UV"," ":" ","@":"@","?":"? OWO",",":",",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"! uwu","(":"(",")":")","\n":"\n"}
cuneiform = {"A":"𒀀","a":"𒀀","B":"𒀉","b":"𒀉","C":"𒀖","c":"𒀖","D":"𒀣","d":"𒀣","E":"𒀯","e":"𒀯","F":"𒀮","f":"𒀮","G":"𒀭","g":"𒀭","H":"𒀬","h":"𒀬","I":"𒀫","i":"𒀫","J":"𒀤","j":"𒀤","K":"𒀟","k":"𒀟","L":"𒁈","l":"𒁈","M":"𒁎","m":"𒁎","N":"𒁠","n":"𒁠","O":"𒁱","o":"𒁱","P":"𒁾","p":"𒁾","Q":"𒂏","q":"𒂏","R":"𒂡","r":"𒂡","S":"𒂶","s":"𒂶","T":"𒃆","t":"𒃆","U":"𒄀","u":"𒄀","V":"𒄒","v":"𒄒","W":"𒄖","w":"𒄖","X":"𒄢","x":"𒄢","Y":"𒄱","y":"𒄱","Z":"𒄼","z":"𒄼"," ":" ","@":"@","?":"¿",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"!","(":"(",")":")",",":",","\n":"\n"}
morse = {"A":".- ","a":".- ","B":"-... ","b":"-... ","C":"-.-. ","c":"-.-. ","D":"-.. ","d":"-.. ","E":". ","e":". ","F":"..-. ","f":"..-. ","G":"--. ","g":"--. ","H":".... ","h":".... ","I":".. ","i":".. ","J":".--- ","j":".--- ","K":"-.- ","k":"-.- ","L":".-.. ","l":".-.. ","M":"-- ","m":"-- ","N":"-. ","n":"-. ","O":"--- ","o":"--- ","P":".--. ","p":".--. ","Q":"--.- ","q":"--.- ","R":".-. ","r":".-. ","S":"... ","s":"... ","T":"- ","t":"- ","U":"..- ","u":"..- ","V":"...- ","v":"...- ","W":".-- ","w":".-- ","X":"-..- ","x":"-..- ","Y":"-.-- ","y":"-.-- ","Z":"--.. ","z":"--.. "," ":"/ ","@":".--.-. ","?":"..--.. ",".":".-.-.- ","/":"-..-. ",":":"---... ",",":"--..--","<":"<","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",">":">","!":"-.-.-- ","(":"-.--. ",")":"-.--.- ","\n":"\n"}
aesthetic = {"A":"𝒜","a":"𝒶","B":"𝐵","b":"𝒷","C":"𝒞","c":"𝒸","D":"𝒟","d":"𝒹","E":"𝐸","e":"𝑒","F":"𝐹","f":"𝒻","G":"𝒢","g":"𝑔","H":"𝐻","h":"𝒽","I":"𝐼","i":"𝒾","J":"𝒥","j":"𝒿","K":"𝒦","k":"𝓀","L":"𝐿","l":"𝓁","M":"𝑀","m":"𝓂","N":"𝒩","n":"𝓃","O":"𝒪","o":"𝑜","P":"𝒫","p":"𝓅","Q":"𝒬","q":"𝓆","R":"𝑅","r":"𝓇","S":"𝒮","s":"𝓈","T":"𝒯","t":"𝓉","U":"𝒰","u":"𝓊","V":"𝒱","v":"𝓋","W":"𝒲","w":"𝓌","X":"𝒳","x":"𝓍","Y":"𝒴","y":"𝓎","Z":"𝒵","z":"𝓏"," ":" ","!":"!","?":"?","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0","\n":"\n","(":"(",")":")",",":",","/":"/","\\":"\\",":":":","@":"@",".":"."}

#-######################################################################
#-########## BOT STARTS HERE ###########################################
#-######################################################################
extensions = ["cogs.moderation","cogs.general","cogs.fun","cogs.computer"]
# On ready
@client.event
async def on_ready():
    print("The doorbell rang...")
    #print([guild for guild in client.guilds])
    # Set presence
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}[command]"))
@client.command(name="reload", description="Reloads extension.")
async def reload(ctx, content):
    # checks if the entered extension is a valid extension
    if content not in extensions:
        if content == "all":
            for extension in extensions:
                await ctx.send(f"Reloading extension {extension}...")
                client.reload_extension(extension)
                await ctx.send(f"Reloaded extension {extension}. May have failed; check the logs!")
        else:
            await ctx.send(f"Extension not found. Here are a list of extensions:\n{extensions}")
    else:
        # if it is valid then reload.
        await ctx.send(f"Reloading extension {content}...")
        client.reload_extension(content)
        await ctx.send(f"Reloaded extension {content}. May have failed; check the logs!")
@client.command(name="cv", description="Change DingDong's avatar.")
async def avchanger(ctx):
    if ctx.message.attachments == []:
        await ctx.send("DingDong only accepts Discord attachments attached on the same message.")
        return
    if ctx.message.attachments != []:
        attachment = ctx.message.attachments[0]
        if attachment.content_type[0:5] == "image":
            await attachment.save("dingdongavatar.png")
            with open("dingdongavatar.png", "rb") as pic:
                pfp = pic.read()
            await client.user.edit(avatar=pfp)
            await ctx.send("Avatar changed.")
        else:
            await ctx.send("Please attach a compatible image file.")
@avchanger.error
async def avchanger_error(ctx,error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Sorry, but Discord restricts bots to changing their avatar 2 times with a 10 minute cooldown.")
# Message delete
@client.event
async def on_message_delete(message):
    channel = await client.fetch_channel(713855953782702103)
    await channel.send(f"Someone tried to delete a message.\nAuthor: {message.author}\nMessage: {message.content}\nMessage created at: {message.created_at}\nChannel: #{message.channel}\nGuild: {message.guild}")
    if message.attachments != []:
        await channel.send(message.attachments[0].url)
# Message edit
@client.event
async def on_message_edit(message, nmessage):
    channel = await client.fetch_channel(713855953782702103)
    if message.edited_at == None:
        await channel.send(f"Someone tried to edit their message.\nAuthor: {message.author}\nOriginal message: {message.content}\nNew message: {nmessage.content}\nOriginal time: {message.created_at}\nTime of edit: No prior edits\nChannel: #{message.channel}\nGuild: {message.guild}")
        if message.attachments != []:
            await channel.send(message.attachments[0].url)
    else:
        await channel.send(f"Someone tried to edit their message.\nAuthor: {message.author}\nOriginal Message: {message.content}\nNew message: {nmessage.content}\nOriginal time: {message.created_at}\nTime of edit: {message.edited_at}\nChannel: #{message.channel}\nGuild: {message.guild}")
        if message.attachments != []:
            await channel.send(message.attachments[0].url)
if __name__ == "__main__":
    # load extensions on startup
    for extension in extensions:
        client.load_extension(extension)
else:
    raise(RuntimeError("Run the bot directly."))
client.run(token)
