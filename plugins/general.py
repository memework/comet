from utils import checks
from discord.ext import commands
from datetime import datetime
class General:
	"""Example plugin!"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@checks.is_dev()
	async def restart(self, ctx):
		"""Reboot the bot, check pm2 logs if the bot doesnt come back online"""
		await ctx.send("Bot is restarting... one moment")
		await self.bot.logout()
	@commands.command()
	async def ping(self, ctx):
		"""Replies with pong"""
		bawt = await ctx.send('Pong')
		#breaking up the vomit so i can piece it later -c
		spaghettivomit = (datetime.now() - bawt.created_at).total_seconds() * 1000
		await bawt.edit(content="Pong! Took " + str(round(spaghettivomit, 1)) + " ms")
def setup(bot):
	bot.add_cog(General(bot))

