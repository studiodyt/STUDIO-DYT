from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(activity=discord.Streaming(name="BREAK THE MODL / STUDIODYT.", url='https://discord.gg/MGGPNMNWXs'))

@client.event
async def on_message(message):

    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="STUDIO DYT / VERIFY", description="정상적으로 인증처리 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 요청자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="PROJECT BY. STUDIO DYT.")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = 'MEMBER || 맴버')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="STUDIO DYT / VERIFY", description = message.author.mention + "님은 인증대상자가 아닙니다.", color = 0xff0000))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
