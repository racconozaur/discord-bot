import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "!", intents = discord.Intents.all())

main_word = ['hello bot'] # the message to which the bot will reply 

# message when running a bot
@client.event
async def on_ready():
    print("Hi")

# reply to the message
@client.event
async def on_message( message ):
    msg = message.content.lower()

    if msg in main_word:
        await  message.channel.send('hello dude')

# gives role and sends welcome message
@client.event
async def on_member_join( member ):
    channel = client.get_channel( 0 ) # id of a channel where the welcome message will be sended

    role = discord.utils.get( member.guild.roles, id = 0 ) # id of a role which will be given by bot when the new person will join to the server
    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description= f'Hi ``{ member.name}``, wlcome to our server', color= 0xFFCCCC))

# run bot
TOKEN = ' 0 ' # bots token  
client.run(TOKEN)