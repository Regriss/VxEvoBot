# Created By GoDzy

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='^')
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Avviato con successo!")
    await bot.change_presence(game=discord.Game(name="^comandi"))

# Comandi

@bot.command(pass_context=True)
async def comandi(ctx):
    embed=discord.Embed(title=":page_facing_up:**Qui vedrai tutti i comandi!**:page_facing_up:", color=0xff8000)
    embed.add_field(name="▶ __𝐒𝐭𝐚𝐟𝐟__ :sparkles:", value="**|** ` ^info ` **|** ` ^crea ` **|** ` ^serverinfo ` **|**", inline=True)
    embed.add_field(name="▶ __𝐈𝐧𝐟𝐨__ :pushpin: ", value="**|** `^staff` **|** `^membri` **|**", inline=False)
    embed.set_footer(text="^comandi")
    await bot.say(embed=embed)

# Info

@bot.command(pass_context=True)
async def staff(ctx):
    embed=discord.Embed(title="Qui vedrai tutto lo STAFF!:point_down:", color=0xffff00)
    embed.add_field(name="➤ 𝐅𝐨𝐮𝐧𝐝𝐞𝐫", value=" `eXoTic Climatic e eXoTic Fil` ", inline=False)
    embed.add_field(name="➤ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", value=" `eXoTic Regriss` ", inline=False)
    embed.add_field(name="➤ 𝐀𝐝𝐦𝐢𝐧", value=" `eXoTic ROM3` ", inline=False)
    embed.set_footer(text="Invita i tuoi amici! \
    https://discord.gg/WyQ6uNd")
    await bot.say(embed=embed, delete_after=5)

# Info

@bot.command(pass_context=True)
async def team(ctx):
    embed=discord.Embed(title=":crossed_swords: `Ecco i membri del Team! :crossed_swords:", color=0x8000ff)
    embed.add_field(name="**eXoTic Climatic**", value="** **", inline=False)
    embed.add_field(name="**eXoTic Fil**", value="** **", inline=False)
    embed.add_field(name="**eXoTic Regriss**", value="** **", inline=False)
    embed.add_field(name="**eXoTic ROM3**", value="** **", inline=False)
    await bot.say(embed=embed)

# Staff

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed=discord.Embed(name="{}prova".format(ctx.message.server.name), color=0x00ff00)
    embed.set_author(name="**Info sul Server:**")
    embed.add_field(name="`𝐍𝐨𝐦𝐞 𝐝𝐞𝐥 𝐒𝐞𝐫𝐯𝐞𝐫:`", value=ctx.message.server.name, inline=True)
    embed.add_field(name="`𝐈𝐃 𝐝𝐞𝐥 𝐒𝐞𝐫𝐯𝐞𝐫:`", value=ctx.message.server.id, inline=True)
    embed.add_field(name="`𝐑𝐮𝐨𝐥𝐢:`", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="`𝐌𝐞𝐦𝐛𝐫𝐢 𝐜𝐨𝐧𝐧𝐞𝐬𝐬𝐢:`", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

# Staff

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    if "♘ admin's" in [y.name.lower() for y in ctx.message.author.roles]:
        embed=discord.Embed(title="**Info su {}.**".format(user.name), color=0x00ff00)
        embed.add_field(name="`𝐍𝐨𝐦𝐞:`", value=user.name, inline=False)
        embed.add_field(name="`𝐈𝐃:`", value=user.id, inline=True)
        embed.add_field(name="`𝐒𝐭𝐚𝐭𝐨:`", value=user.status, inline=True)
        embed.add_field(name="`𝐑𝐮𝐨𝐥𝐨 𝐩𝐢𝐮' 𝐚𝐥𝐭𝐨:`", value=user.top_role)
        embed.add_field(name="`𝐄𝐧𝐭𝐫𝐚𝐭𝐨 𝐢𝐥:`", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.say(embed=embed)
    else:
        await bot.send_message(ctx.message.channel, "Devi avere il ruolo Admin per usare questo comando!")

# Staff

@bot.command(pass_context=True, description='Prova')
async def crea(ctx, channel_type, name):
    msg = ctx.message
    server = msg.server
    channel_type_map = {
        'ctestuale': discord.ChannelType.text,
        'cvocale': discord.ChannelType.voice
    }
    if channel_type not in channel_type_map:
        await bot.say('Prova a fare il comando \"^create Testuale\" o \"^create Vocale\".', delete_after=5)
        return
    Palloso = discord.PermissionOverwrite()
    mine = discord.PermissionOverwrite(manage_channels=True, manage_roles=True, move_members=True)
    try:
        await bot.create_channel(msg.server, name, (server.default_role, Palloso), (msg.author, mine), type=channel_type_map[channel_type])
        await bot.say('{0}, ha creato la stanza: \"{2}\".'.format(msg.author, channel_type, name))
    except Exception as e:
        await bot.say('Impossibile creare la stanza'.format(e))

# Staff

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    if "exotic team" in [y.name.lower() for y in ctx.message.author.roles]:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
        await bot.say("Messaggi cancellati.", delete_after=2)
    else:
        await bot.send_message(ctx.message.channel, "Devi avere il ruolo Admin per usare questo comando!")

bot.run(process.env.BOT_TOKEN);
