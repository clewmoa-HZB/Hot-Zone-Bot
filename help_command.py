import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View
import json
import asyncio

class HelpCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@app_commands.command(name="help", description="Affiche l'aide pour les commandes.")
	@app_commands.describe(
		command="Nom de la commande pour afficher les détails.",
		group="Nom du groupe pour afficher les commandes associées."
	)
	async def help(self, interaction: discord.Interaction, command: str = None, group: str = None):
		# Charger les données depuis commands.json
		try:
			with open("Files/Data/Commands/commands.json", "r", encoding="utf-8") as file:
				commands_data = json.load(file)
		except FileNotFoundError:
			await interaction.response.send_message("Le fichier des commandes est introuvable.", ephemeral=True)
			return
		except json.JSONDecodeError:
			await interaction.response.send_message("Le fichier des commandes est corrompu.", ephemeral=True)
			return

		# Gestion des cas
		if not command and not group:
			# Aucun groupe ni commande précisé : afficher les groupes disponibles avec un sélecteur
			select = Select(
				placeholder="Choisissez un groupe de commandes",
				options=[
					discord.SelectOption(label=grp, description=f"Voir les commandes du groupe {grp}")
					for grp in commands_data.keys()
				]
			)

			async def select_callback(interaction: discord.Interaction):
				selected_group = select.values[0]
				embed = discord.Embed(
					title=f"Commandes du groupe {selected_group}",
					description="Voici les commandes disponibles dans ce groupe :",
					color=discord.Color.blue()
				)
				for cmd in commands_data[selected_group]:
					embed.add_field(name=cmd["name"], value=cmd["description"], inline=False)
				await interaction.response.edit_message(embed=embed, view=None)

			select.callback = select_callback

			view = View()
			view.add_item(select)

			embed = discord.Embed(
				title="Groupes disponibles",
				description="Veuillez choisir un groupe dans le menu déroulant ci-dessous :",
				color=discord.Color.blue()
			)
			await interaction.response.send_message(embed=embed, view=view, ephemeral=False)

		elif group and not command:
			# Un groupe est précisé : afficher les commandes du groupe
			if group not in commands_data:
				await interaction.response.send_message(f"Le groupe `{group}` n'existe pas.", ephemeral=True)
				return

			embed = discord.Embed(
				title=f"Commandes du groupe {group}",
				description="Voici les commandes disponibles dans ce groupe :",
				color=discord.Color.blue()
			)
			for cmd in commands_data[group]:
				embed.add_field(name=cmd["name"], value=cmd["description"], inline=False)
			await interaction.response.send_message(embed=embed, ephemeral=True)

		elif command and not group:
			# Une commande est précisée : afficher les détails de la commande
			found = None
			for grp, cmds in commands_data.items():
				for cmd in cmds:
					if cmd["name"] == command:
						found = cmd
						break
				if found:
					break

			if not found:
				await interaction.response.send_message(f"La commande `{command}` n'existe pas.", ephemeral=True)
				return

			embed = discord.Embed(
				title=f"Détails de la commande {command}",
				color=discord.Color.blue()
			)
			embed.add_field(name="Description", value=found["description"], inline=False)
			embed.add_field(name="Paramètres", value=json.dumps(found.get("parameters", {}), indent=2), inline=False)
			embed.add_field(name="Effets", value=found.get("effects", "Aucun effet spécifié."), inline=False)
			message = await interaction.response.send_message(embed=embed, ephemeral=True)

		else:
			# Un groupe et une commande sont précisés : erreur
			await interaction.response.send_message(
				"Vous ne pouvez pas spécifier un groupe et une commande en même temps.", ephemeral=True
			)
			return

		# Supprimer le message après 30 secondes d'inactivité
		await asyncio.sleep(30)
		try:
			await message.delete()
		except discord.NotFound:
			pass

	@help.autocomplete("group")
	async def group_autocomplete(self, interaction: discord.Interaction, current: str):
		# Fournir les groupes disponibles pour l'autocomplétion
		try:
			with open("Files/Data/Commands/commands.json", "r", encoding="utf-8") as file:
				commands_data = json.load(file)
			return [app_commands.Choice(name=grp, value=grp) for grp in commands_data.keys() if current.lower() in grp.lower()]
		except:
			return []

	@help.autocomplete("command")
	async def command_autocomplete(self, interaction: discord.Interaction, current: str):
		# Fournir les commandes disponibles pour l'autocomplétion
		try:
			with open("Files/Data/Commands/commands.json", "r", encoding="utf-8") as file:
				commands_data = json.load(file)
			commands = [cmd["name"] for cmds in commands_data.values() for cmd in cmds]
			return [app_commands.Choice(name=cmd, value=cmd) for cmd in commands if current.lower() in cmd.lower()]
		except:
			return []

async def setup(bot):
	await bot.add_cog(HelpCommand(bot))