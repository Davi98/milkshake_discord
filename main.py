
from dotenv import load_dotenv
import os
import discord
from discord.utils import get
from discord import Intents



load_dotenv()
intents = Intents.all()
client = discord.Client(intents=intents)

embed_role = discord.Embed(title='SELECIONE SUA ROLE',
                    description="Reaja de acordo com sua lane principal do League of Legends:\n\n<:toplane:960929409781612596> Top Lane \n\n <:jungle:960927465247756328> Jungle \n\n <:mid:960928365097943080>  Mid Lane\n\n <:adc:960928614797410364>  Adcarry\n\n <:suporte:960929564496904193> Suporte",
                    color=0x0089d6) 

embed_elo = discord.Embed(title='SELECIONE SEU ELO',
                    description="Reaja de acordo com seu elo atual no League of Legends:\n\n<:challenger:960933200841027614> Challenger\n\n<:GM:960933117357588590> Grão-Mestre\n\n<:mestre:960933348157587516> Mestre\n\n<:diamante:960933117189841026> Diamante\n\n<:platina:960933116820750356> Platina\n\n<:ouro:960933879978549288> Ouro\n\n<:prata:960933347675217952> Prata\n\n<:bronze:960933348426010674>Bronze\n\n<:ferro:960936086572531813> Ferro",
                    color=0x0089d6)

embed_post = discord.Embed(title='Qual a sua ligação com a Rising Tide?',
                    description="🕹️ Sou Jogador\n\n👓 Sou parte da Staff\n\n💙 Sou visitante",
                    color=0x0089d6)

@client.event
async def on_ready():
    channel = client.get_channel(int(os.environ.get('CHANNEL_ID')))
    if bool(os.environ.get("FIRST_TIME",False)):
        message_1 = await channel.send(embed=embed_role)
        await message_1.add_reaction('<:toplane:960929409781612596>')
        await message_1.add_reaction('<:jungle:960927465247756328>')
        await message_1.add_reaction('<:mid:960928365097943080>')
        await message_1.add_reaction('<:adc:960928614797410364>')
        await message_1.add_reaction('<:suporte:960929564496904193>')
        
        message_2 = await channel.send(embed=embed_elo)
        await message_2.add_reaction('<:challenger:960933200841027614>')
        await message_2.add_reaction('<:GM:960933117357588590>')
        await message_2.add_reaction('<:mestre:960933348157587516>')
        await message_2.add_reaction('<:diamante:960933117189841026>')
        await message_2.add_reaction('<:platina:960933116820750356>')
        await message_2.add_reaction('<:ouro:960933879978549288>')
        await message_2.add_reaction('<:prata:960933347675217952>')
        await message_2.add_reaction('<:bronze:960933348426010674>')
        await message_2.add_reaction('<:ferro:960936086572531813>')

        message_3 = await channel.send(embed=embed_post)
        await message_3.add_reaction('🕹️')
        await message_3.add_reaction('👓')
        await message_3.add_reaction('💙')
    

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = get(guild.members, id=payload.user_id)
    if payload.channel_id == int(os.environ['CHANNEL_ID']) and payload.message_id == int(os.environ['MESSAGE_ID']):
        if str(payload.emoji) == "🕹️":
            role = get(member.guild.roles, name='Rising Tide Tridents')
        elif str(payload.emoji) == "👓":
            role = get(member.guild.roles, name='Staff')
        elif str(payload.emoji) == "💙":
            role = get(member.guild.roles, name='Visitante')
        else:
            role = get(guild.roles, name=payload.emoji)

        if role is not None:
            await payload.member.add_roles(role)
            print(f"Assigned {member} to {role}.")

@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = get(guild.members, id=payload.user_id)
    print(member)
    if payload.channel_id == int(os.environ['CHANNEL_ID']) and payload.message_id == int(os.environ['MESSAGE_ID']):
        if str(payload.emoji) == "🕹️":
            role = get(member.guild.roles, name='Rising Tide Tridents')
        elif str(payload.emoji) == "👓":
            role = get(member.guild.roles, name='Staff')
        elif str(payload.emoji) == "💙":
            role = get(guild.roles, name='Visitante')
        else:
            role = get(guild.roles, name=payload.emoji)

        if role is not None:
            await member.remove_roles(role)
            print(f"Removed {role} from {member}.")


print("Server Running.")


client.run(os.environ.get("TOKEN"))