import sqlite3 as sql3
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

help_array = ["help", "привет", "помощь", "команды", "как", 'info', "инфо", "commands", "command"]

def get_list(name_table):
    conn = sql3.connect("base.db")
    cursor = conn.cursor()

    cursor.execute(f"select * from {name_table} ")

    name_list = cursor.fetchall()
    return name_list

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def info(ctx):
    emb = discord.Embed(title="Команды")
    emb.add_field(name="1)", value=".algo +/-", inline=False)
    emb.add_field(name="2)", value=".discret +/-", inline=False)
    await ctx.send(embed=emb)

@client.command(pass_context=True)
async def algo(ctx, *, command):

    conn = sql3.connect("base.db")
    cursor = conn.cursor()

    name = ctx.message.author.mention

    if "+" in command:
        cursor.execute(f"select fio from queue where fio = '{name}'")
        flag = cursor.fetchone()

        if flag:
            await ctx.send(f"{name} присутствует в таблице Алгосы")
        else:
            name_list_0 = get_list("queue")

            cursor.execute(f"insert into queue (fio, possition) values ('{name}', '{1}')")
            conn.commit()

            await ctx.send(f"{name} добавлен в таблицу Алгосы")

            name_list = get_list("queue")
            emb = discord.Embed(title="Список Алгосы")

            for i in name_list:
                emb.add_field(name=i[1], value=i[0], inline=False)

            await ctx.send(embed=emb)

    if "-" in command:
        cursor.execute(f"select fio from queue where fio = '{name}'")
        flag = cursor.fetchone()

        if not flag:
            await ctx.send(f"{name} отсутствует в таблице Алгосы")

        else:
            cursor.execute(f"delete from queue where fio = '{name}'")
            conn.commit()

            await ctx.send(f"{name} удален из таблица Алгосы")

            name_list = get_list("queue")

            emb = discord.Embed(title="Список Алгосы")

            for i in name_list:
                emb.add_field(name=i[1], value=i[0], inline=False)

            await ctx.send(embed=emb)

@client.command(pass_context=True)
async def discret(ctx, *, command):

    conn = sql3.connect("base.db")
    cursor = conn.cursor()

    name = ctx.message.author.mention

    if "+" in command:
        cursor.execute(f"select fio from discretka where fio = '{name}'")
        flag = cursor.fetchone()

        if flag:
            await ctx.send(f"{name} присутствует в таблице Дискретка")
        else:
            name_list_0 = get_list("discretka")

            cursor.execute(f"insert into discretka (fio, possition) values ('{name}', '{1}')")
            conn.commit()

            await ctx.send(f"{name} добавлен в таблицу Дискретка")

            name_list = get_list("discretka")
            emb = discord.Embed(title="Список Дискретка")

            for i in name_list:
                emb.add_field(name=i[1], value=i[0], inline=False)

            await ctx.send(embed=emb)

    if "-" in command:
        cursor.execute(f"select fio from discretka where fio = '{name}'")
        flag = cursor.fetchone()

        if not flag:
            await ctx.send(f"{name} отсутствует в таблице Дискретка")

        else:
            cursor.execute(f"delete from discretka where fio = '{name}'")
            conn.commit()

            await ctx.send(f"{name} удален из таблицы Дискретка")

            name_list = get_list("discretka")

            emb = discord.Embed(title="Список Дискретка")

            for i in name_list:
                emb.add_field(name=i[1], value=i[0], inline=False)

            await ctx.send(embed=emb)

client.run("Ваш токен")
