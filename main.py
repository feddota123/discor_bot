import discord
from discord.ext import commands
import pyttsx3
from bs4 import BeautifulSoup
import requests
import asyncio
import random
from config import TOKEN

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.command(name='move')
@commands.has_permissions(administrator = True)
async def move(ctx, channel: discord.VoiceChannel = None, channel2: discord.VoiceChannel = None, member: discord.Member = None):
    await ctx.message.delete()
    if channel == None:
        pass
    elif channel2 == None:
        pass
    elif member == None:
        x = channel.members
        for member in x:
            await member.edit(voice_channel=channel2)
    else: await member.edit(voice_channel=channel2)


@bot.command(name='clear', pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
	await ctx.message.delete()  # Удаляет написанное вами сообщение
	await ctx.channel.purge(limit=amount)  # удаляет сообщения
	em = discord.Embed(description=f'было удаленно *{amount}* сообщений', color=708090)  # настройка embed
	await ctx.send(embed=em)  # вставка embed
	await asyncio.sleep(3)  # таймер ожидания
	await ctx.channel.purge(limit=1)  # Удаляет сообщение бота


@bot.command(name='mute')
async def mute(ctx, member : discord.Member = None):
    await ctx.message.delete()
    if not member:
        ctx.send("Укажите пользователя!")
    else:
        membern = member.nick
        if member.nick == None:
            membern = member.name
        unmute_cnt = f"Пользователь {membern} был замучен админом {ctx.author}!"
        unmute = discord.Embed(title= "Mute", description= unmute_cnt, colour= 0x000000)
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role)
        await ctx.send(embed=unmute)


@bot.command(name='unmute')
async def unmute(ctx, member : discord.Member = None):
    await ctx.message.delete()
    if not member:
        ctx.send("Укажите пользователя!")
    else:
        membern = member.nick
        if member.nick == None:
            membern = member.name
        unmute_cnt = f"Пользователь {membern} был раззамучен админом {ctx.author}!"
        unmute = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x000000)
        role = discord.utils.get(ctx.message.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(embed= unmute)


@bot.command(name='say')
@commands.has_permissions(administrator = True)
async def say(ctx, *args):
    await ctx.message.delete()
    args = ''.join(args).split('/', maxsplit = 1)
    try:
        user = bot.get_user(int(args[0][args[0].find("!") + 1 : -1]))
        await user.send(args[1])
    except:
        await ctx.send(args[0])


@bot.command(name='random')
@commands.has_permissions(administrator = True)
async def say_a(ctx, *args):
    users = []
    for m in ctx.guild.members:
        if m.bot: continue
        users.append(str(m))
    await ctx.channel.send('Случайный человек: ' + random.choice(users))


@bot.command(pass_context=True, name='ping', brief='Показать текущую задержку')
@commands.cooldown(1, 1, commands.BucketType.user)
async def ping(ctx):
	try:
		await ctx.message.delete()
	except:
		pass
	em = discord.Embed(title='**Текущая задержка:**', description=f'``{bot.ws.latency * 1000:.0f} ms``')
	em.set_author(name=f'Ping', icon_url=bot.user.avatar_url)
	em.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
	await ctx.send(embed=em)

@bot.command(name='coin')
async def coin(ctx):
    num=random.randint(1,2)
    if (num == 1):
           await ctx.send("Вым выпал - Орёл")
           print("[?coin] - done")
    if(num == 2):
           await ctx.send("Вам выпала - Решка")
           print("[?coin] - done")


@bot.event
async def on_ready():
	print("online")

print('Bot by RZ')
bot.run(TOKEN)
