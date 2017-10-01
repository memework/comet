#Plugin system inspired from one of my earlier creations, Knarrenhienz -C


#imports the checks function
from utils import checks
import utils.clark as clark
from ruamel.yaml import YAMLError

from discord.ext import commands

class Core:
	"""Core functions of the bot, includes plugins"""
	def __init__(self, bot):
		self.bot = bot
		bot.log.info("loading plugins...")
		try:
			self.plugins = clark.load('config/plugins.yml')
		except YAMLError as exc:
			raise Exception('Invalid yaml, wtf!')
		except FileNotFoundError:
			bot.log.warning("file not found, creating new plugin config!")
			self.plugins = []
			clark.save(self.plugins, "config/plugins.yml")
		for i in self.plugins:
			try:
				self.bot.load_extension("plugins." + i)
				bot.log.info("%s loaded sucessfuly" % i)
			except Exception as e:
				self.plugins.remove(i)
				bot.log.error("{}: {}".format(i, e))
				clark.save(self.plugins, "config/plugins.yml")
				bot.log.warn("{} unloaded due to errors, load it when it works again".format(i))

		bot.log.info("%i plugins loaded" % len(self.plugins))

	@checks.is_dev()
	@commands.command(name="plugins")
	async def loaded(self, ctx):
		"""lists loaded plugins"""
		await ctx.send("```\nPlugins:\n{}```".format(', '.join(self.plugins)))

	@checks.is_dev()
	@commands.command()
	async def reload(self, ctx, name):
		"""reloads a plugin"""
		if name == "core":
			await ctx.send("you cant just reload the core!")
			return
		try:
			self.bot.unload_extension("plugins." + name)
			self.bot.log.info("unloaded "+name)
		except Exception as e:
			await ctx.send("failed to reload plugin: {}".format(e))
		try:
			self.bot.load_extension("plugins." + name)
			self.bot.log.info("reloaded "+name+" sucessfully")
			await ctx.send("plugin reloaded sucessfuly")
		except Exception as e:
			await ctx.send("failed to load plugin: {}".format(e))
			if name in self.plugins:
				self.plugins.remove(name)
				await ctx.send("I see that {} is in your loaded plugins, I will unload it for now since it has errors".format(name))
				clark.save(self.plugins, "config/plugins.yml")
	@checks.is_dev()
	@commands.command()
	async def load(self, ctx, name):
		"""loads a plugin"""
		if name == "core":
			await ctx.send("core is already loaded by default!")
			return
		if name in self.plugins:
			await ctx.send("plugin is already loaded")
			return
		try:
			self.bot.load_extension("plugins." + name)
			self.plugins.append(name)
			clark.save(self.plugins, "config/plugins.yml")
			await ctx.send("plugin loaded sucessfuly")
			self.bot.log.info("Plugin "+name+" loaded.")
		except Exception as e:
			await ctx.send("failed to load plugin: {}".format(e))
			self.bot.log.error("failed to load plugin: {}".format(e))

	@checks.is_dev()
	@commands.command()
	async def unload(self, ctx, name):
		"""unloads a plugin"""
		if name == "core":
			await ctx.send("unloading the core is disabled")
			return
		try:
			self.bot.unload_extension("plugins." + name)
			self.plugins.remove(name)
			clark.save(self.plugins, "config/plugins.yml")
			await ctx.send("plugin unloaded sucessfuly")
			self.bot.log.info("plugin "+name+" loaded")
		except Exception as e:
			await ctx.send("failed to load plugin: {}".format(e))
			self.bot.log.error("failed to load plugin: {}".format(e))
def setup(bot):
	bot.add_cog(Core(bot))
