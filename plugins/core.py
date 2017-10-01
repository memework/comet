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
		print("loading plugins...")
		try:
			self.plugins = clark.load('config/plugins.yml')
		except YAMLError as exc:
			raise Exception('Invalid yaml, wtf!')
		except FileNotFoundError:
			print("file not found, creating new plugin config!")
			self.plugins = []
			clark.save(self.plugins, "config/plugins.yml")
		for i in self.plugins:
			try:
				self.bot.load_extension("plugins." + i)
				print("[ \033[0;32mdone\033[0;0m ] %s loaded sucessfuly" % i)
			except Exception as e:
				self.plugins.remove(i)
				print("[ \033[1;31mfail\033[0;0m ] {}: {}".format(i, e))
				clark.save(self.plugins, "config/plugins.yml")
				print("[ \033[1;96mwarn\033[0;0m ] {} unloaded due to errors, load it when it works again".format(i))

		print("%i plugins loaded" % len(self.plugins))

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
			print("unloaded "+name)
		except Exception as e:
			await ctx.send("failed to reload plugin: {}".format(e))
		try:
			self.bot.load_extension("plugins." + name)
			print("reloaded "+name+" sucessfully")
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
		except Exception as e:
			await ctx.send("failed to load plugin: {}".format(e))

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
		except Exception as e:
			await ctx.send("failed to load plugin: {}".format(e))
def setup(bot):
	bot.add_cog(Core(bot))
