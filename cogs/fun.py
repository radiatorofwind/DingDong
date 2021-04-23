import discord
from discord.ext import commands
import os
import json
from discord.ext.commands import Cog
config = os.path.abspath('./config.json')
with open(str(config), "r") as cfg:
    cont = cfg.read()
    jso = json.loads(cont)
    prefix = jso["prefix"]
evalwhitelist = [584194375509344256, 207358306451193857]
client = commands.Bot(command_prefix=prefix)
class FunStuff(commands.Cog):
    def __init__(self, client):
        self.client = client
        print("Fun stuff loaded!")
    @commands.command(name="av", description="Get someone's avatar")
    async def avgetter(ctx, member: discord.Member):
        embed = discord.Embed(title=f"{member.display_name}'s avatar")
        pfp = member.avatar_url
        embed.set_image(url=pfp)
        await ctx.send(embed=embed)
    @commands.command(name="reddit", description="Reddit posts! Pulls from whatever subreddit\nyou post.", aliases=["r"])
    async def redditt(self, ctx, content):
        print(content)
        try:
            sublist = []
            rsubreddit = content
            if content[0:2] == "r/":
                rsubreddit = content[2:]
            subreddit = await reddit.subreddit(rsubreddit)
            async for s in subreddit.hot(limit=500):
                sublist.append(s)
            submission = random.choice(sublist)
            if submission.over_18:
                await ctx.send("Sorry, but the post accessed was NSFW, and as such, can't be displayed here.")
            elif subreddit.over18:
                await ctx.send("Sorry, but the subreddit accessed was NSFW, and as such, can't be displayed here.")
            else:
                redditdate = datetime.fromtimestamp(
                    int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')
                embed = discord.Embed(
                    title=f"From r/{submission.subreddit}", color=0xf7f7f7)
                embed.add_field(name="Post Title:",
                                value=submission.title, inline=False)
                if submission.selftext != "":
                    if len(submission.selftext) > 1024:
                        embed.add_field(name="Selftext:",
                                        value=f"See attached", inline=False)
                        with open("selftext.txt", "w") as file:
                            file.write(stext)
                    else:
                        embed.add_field(
                            name="Selftext:", value=f"{submission.selftext}", inline=False)
                        embed.add_field(name="Original Poster:",
                                        value=f"u/{submission.author}", inline=False)
                        embed.add_field(name="Upvote Percentage:",
                                        value=f"{submission.upvote_ratio}% Upvoted", inline=False)
                        embed.add_field(name="Posted At:",
                                        value=f"{redditdate}")
                        embed.add_field(name="Post URL:",
                                        value=submission.url, inline=False)
                        await ctx.message.channel.send(embed=embed)
                        await ctx.message.channel.send(f"{submission.url}")
                        if len(submission.selftext) > 1024:
                            await ctx.message.channel.send(file=discord.File('selftext.txt'))
                        print(submission.media)
        except ValueError as e:
            print("Reddit command failed: Subreddit not recognized")
            await ctx.send("Something went wrong, sorry.")
    @commands.command(name="keyboard", description=f"Change keyboard! Only available for people with the 'administrator' permission. It deletes messages and replaces letters based on the keyboard selected.\nSyntax: {prefix}keyboard toggle - Turns keyboard on and off.\n{prefix}keyboard <keyboard> Change keyboard when on.\nList of current keyboards: edgy, owo, cuneiform")
    async def keyboard(self, ctx, keyb,*,speech):
        global alphabets
        edgy = {"A":"Ä","a":"ą","B":"ß","b":"þ","C":"Ç","c":"ç","D":"Ð","d":"ď","E":"Ę","e":"ę","F":"Ƒ","f":"ƒ","G":"Ģ","g":"ģ","H":"Ħ","h":"ħ","I":"Ĩ","i":"ĭ","J":"ĵ","j":"Ĵ","K":"Ķ","k":"ĸ","L":"Ľ","l":"ľ","M":"Ṁ","m":"ṁ","N":"Ň","n":"ŋ","O":"Œ","o":"œ","P":"Ƥ","p":"ƥ","Q":"Ɋ","q":"ɋ","R":"Ɍ","r":"ɍ","S":"Ṡ","s":"ṡ","T":"Ŧ","t":"ŧ","U":"Ü","u":"ü","V":"V̄","v":"v̄","W":"Ŵ","w":"ŵ","X":"X̱","x":"x̱","Y":"Ƴ","y":"ƴ","Z":"Ƶ","z":"ƶ"," ":" ","@":"@","?":"¿",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"!","(":"(",")":")",",":",","\n":"\n"}
        owospeak = {"A":"A","a":"a","B":"B","b":"b","C":"C","c":"c","D":"D","d":"d","E":"E","e":"e","F":"F","f":"f","G":"G","g":"g","H":"H","h":"h","I":"I","i":"i","J":"J","j":"j","K":"K","k":"k","L":"W","l":"w","M":"M","m":"m","N":"N","n":"n","O":"O","o":"o","P":"P","p":"p","Q":"Q","q":"q","R":"W","r":"w","S":"S","s":"s","T":"T","t":"t","U":"U","u":"u","V":"V","v":"v","W":"W","w":"w","X":"X","x":"x","Y":"Y","y":"y","Z":"Z","z":"z","th":"ff","Th":"Ff","TH":"FF","ove":"uv","Ove":"Uv","OVE":"UV"," ":" ","@":"@","?":"? OWO",",":",",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"! uwu","(":"(",")":")","\n":"\n"}
        cuneiform = {"A":"𒀀","a":"𒀀","B":"𒀉","b":"𒀉","C":"𒀖","c":"𒀖","D":"𒀣","d":"𒀣","E":"𒀯","e":"𒀯","F":"𒀮","f":"𒀮","G":"𒀭","g":"𒀭","H":"𒀬","h":"𒀬","I":"𒀫","i":"𒀫","J":"𒀤","j":"𒀤","K":"𒀟","k":"𒀟","L":"𒁈","l":"𒁈","M":"𒁎","m":"𒁎","N":"𒁠","n":"𒁠","O":"𒁱","o":"𒁱","P":"𒁾","p":"𒁾","Q":"𒂏","q":"𒂏","R":"𒂡","r":"𒂡","S":"𒂶","s":"𒂶","T":"𒃆","t":"𒃆","U":"𒄀","u":"𒄀","V":"𒄒","v":"𒄒","W":"𒄖","w":"𒄖","X":"𒄢","x":"𒄢","Y":"𒄱","y":"𒄱","Z":"𒄼","z":"𒄼"," ":" ","@":"@","?":"¿",".":".","/":"/",":":":","<":"<","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0",">":">","!":"!","(":"(",")":")",",":",","\n":"\n"}
        morse = {"A":".- ","a":".- ","B":"-... ","b":"-... ","C":"-.-. ","c":"-.-. ","D":"-.. ","d":"-.. ","E":". ","e":". ","F":"..-. ","f":"..-. ","G":"--. ","g":"--. ","H":".... ","h":".... ","I":".. ","i":".. ","J":".--- ","j":".--- ","K":"-.- ","k":"-.- ","L":".-.. ","l":".-.. ","M":"-- ","m":"-- ","N":"-. ","n":"-. ","O":"--- ","o":"--- ","P":".--. ","p":".--. ","Q":"--.- ","q":"--.- ","R":".-. ","r":".-. ","S":"... ","s":"... ","T":"- ","t":"- ","U":"..- ","u":"..- ","V":"...- ","v":"...- ","W":".-- ","w":".-- ","X":"-..- ","x":"-..- ","Y":"-.-- ","y":"-.-- ","Z":"--.. ","z":"--.. "," ":"/ ","@":".--.-. ","?":"..--.. ",".":".-.-.- ","/":"-..-. ",":":"---... ",",":"--..--","<":"<","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ",">":">","!":"-.-.-- ","(":"-.--. ",")":"-.--.- ","\n":"\n"}
        aesthetic = {"A":"𝒜","a":"𝒶","B":"𝐵","b":"𝒷","C":"𝒞","c":"𝒸","D":"𝒟","d":"𝒹","E":"𝐸","e":"𝑒","F":"𝐹","f":"𝒻","G":"𝒢","g":"𝑔","H":"𝐻","h":"𝒽","I":"𝐼","i":"𝒾","J":"𝒥","j":"𝒿","K":"𝒦","k":"𝓀","L":"𝐿","l":"𝓁","M":"𝑀","m":"𝓂","N":"𝒩","n":"𝓃","O":"𝒪","o":"𝑜","P":"𝒫","p":"𝓅","Q":"𝒬","q":"𝓆","R":"𝑅","r":"𝓇","S":"𝒮","s":"𝓈","T":"𝒯","t":"𝓉","U":"𝒰","u":"𝓊","V":"𝒱","v":"𝓋","W":"𝒲","w":"𝓌","X":"𝒳","x":"𝓍","Y":"𝒴","y":"𝓎","Z":"𝒵","z":"𝓏"," ":" ","!":"!","?":"?","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0","\n":"\n","(":"(",")":")",",":",","/":"/","\\":"\\",":":":","@":"@",".":"."}
        alphabets = ["owo","edgy","cuneiform","morse","aesthetic"]
        alphabet = edgy
        keyboard = keyb.lower()
        lett = alphabet.keys()
        letty = list(lett)
        y = []
        try:
            if keyboard not in alphabets:
                embed = discord.Embed(title="You seem to be stuck.")
                embed.add_field(name="You typed an invalid keyboard. Here's the available choices:",
                    value=f"{alphabets}", inline=False)
                embed.set_footer(text=f"Non case sensitive")
                await ctx.send(embed=embed)
            else:
                for letter in speech:
                    if letter in letty:                      
                        if keyboard == "owo":
                            alphabet = owospeak
                        elif keyboard == "edgy":
                            alphabet = edgy
                        elif keyboard == "cuneiform":
                            alphabet = cuneiform
                        elif keyboard == "morse":
                            alphabet = morse
                        elif keyboard == "aesthetic":
                            alphabet = aesthetic
                        y.append(alphabet[letter])
                final = ''.join(y)
                y = []
                await ctx.send(final)
        except NameError as e:
            print(e)
    @keyboard.error
    async def keyboard_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="You seem to be stuck.")
            embed.add_field(name="There's 3 arguments to this command:",
                            value=f"{prefix}keyboard [keyboard choice] [speech]", inline=False)
            embed.set_footer(text=f"Available alphabet choices: {alphabets}")
            await ctx.send(embed=embed)
            return
def setup(client):
    client.add_cog(FunStuff(client))
