import discord
from discord.ext import commands
import os
import config


bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print("Bot online!")

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded Cog: {extension}')
        print(f"Loaded Cog from discord: {extension}")
    else:
        await ctx.send("You must be the bot owner to run this command.")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == config.owner_id:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded Cog: {extension}')
        print(f"Unloaded Cog from discord: {extension}")
    else:
        await ctx.send("You must be the bot owner to run this command.")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == config.owner_id:
        if extension == 'all':
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    bot.load_extension(f'cogs.{filename[:-3]}')
                    await ctx.send("Reloaded all cogs.")
                    print("Reloaded all cogs in discord.")
                else:
                    await ctx.send("Error loading __pycache__. you can ignore this error.")
                    print("Error loading __pycache__ you can ignore this error.")
        else:
            bot.reload_extension(f'cogs.{extension}')
            await ctx.send(f'Reloaded Cog: {extension}')
            print(f"Reloaded Cog from discord: {extension}")
    else:
        await ctx.send("You must be the bot owner to run this command.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded cog: {filename[:-3]}")
    else:
        print("Erorr loading __pycache__ you can ignore this error.")


bot.run(config.token)