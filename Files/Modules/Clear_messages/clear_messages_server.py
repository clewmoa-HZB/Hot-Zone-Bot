import discord
from discord.ext import commands
from discord import app_commands

class ClearMessagesServer(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@app_commands.command(name="clear-messages-server", description="Supprime les messages d'un utilisateur sur tout le serveur.")
	@app_commands.describe(user="Utilisateur ciblé", amount="Nombre de messages à supprimer (optionnel)")
	async def clear_messages_server(self, interaction: discord.Interaction, user: discord.User, amount: int = None):
		# Vérifie la permission "Gérer les messages"
		if not interaction.user.guild_permissions.manage_messages:
			await interaction.response.send_message("Vous n'avez pas la permission de gérer les messages.", ephemeral=True)
			return

		await interaction.response.defer(ephemeral=True)
		deleted = 0
		try:
			for channel in interaction.guild.text_channels:
				async for msg in channel.history(limit=1000):
					if msg.author.id == user.id:
						if amount and deleted >= amount:
							break
						await msg.delete()
						deleted += 1
				if amount and deleted >= amount:
					break
			await interaction.followup.send(f"{deleted} message(s) supprimé(s) de {user.mention} sur le serveur.", ephemeral=True)
		except Exception as e:
			await interaction.followup.send(f"Erreur : {e}", ephemeral=True)

async def setup(bot):
	await bot.add_cog(ClearMessagesServer(bot))
