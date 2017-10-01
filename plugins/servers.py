import utils.checks
from discord.ext import commands

class Servers:
	"""Development stuff, I wrote this at 3am because I got bored. Blame my lack of porn on this poorly written module"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@checks.is_dev()
	async def leave(self, ctx, server: int, *, reason="KILL THE INFIDELS!"):
		try:
			server = self.bot.guilds[server]
			await server.owner.send(reason)
			await server.leave()
			await ctx.send("done!")
		except Exception as e:
			await ctx.send("Something fucked up, {}".format(e))
	
	@commands.command()
	@checks.is_dev()
	async def getinv(self, ctx, server: int, *, reason="KILL THE INFIDELS!"):
		try:
			server = self.bot.guilds[server]
			for i in server.channels:
				try:
					x = await i.create_invite(reason=reason)
					break
				except:
					print("failed inv on {}, type {} on server {}".format(i.name, i.__class__.__name__, server.name))
					continue
			if 'x' in locals():
				await ctx.send("discord.gg/"+x.code)
			else:
				await ctx.send("tried all channels, cant get a single inv!")
		except Exception as e:
			await ctx.send("Something fucked up, {}".format(e))
def setup(bot):
	bot.add_cog(Servers(bot))

