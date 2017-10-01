from discord.ext import commands
from __main__ import cfg
def is_dev():
	return commands.check(lambda ctx: check_dev(ctx))
def check_dev(ctx):
	return ctx.message.author.id == cfg['discord']['ownerid']