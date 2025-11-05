import discord
from discord.ext import commands
from discord import app_commands

class ClearMessages(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@app_commands.command(name="clear-messages", description="Supprime un nombre de messages dans le salon. Optionnellement, seulement ceux d'un utilisateur.")
	@app_commands.describe(amount="Nombre de messages à supprimer", user="Utilisateur ciblé (optionnel)")
	async def clear_messages(self, interaction: discord.Interaction, amount: int, user: discord.User = None):
		# Vérifie la permission "Gérer les messages"
		if not interaction.user.guild_permissions.manage_messages:
			await interaction.response.send_message("Vous n'avez pas la permission de gérer les messages.", ephemeral=True)
			return

		await interaction.response.defer(ephemeral=True)
		deleted = 0
		def check(m):
			if user:
				return m.author.id == user.id
			return True
		try:
			deleted_msgs = []
			async for msg in interaction.channel.history(limit=1000):
				if deleted >= amount:
					break
				if check(msg):
					await msg.delete()
					deleted += 1
					deleted_msgs.append(msg)
			await interaction.followup.send(f"{deleted} message(s) supprimé(s) dans ce salon.", ephemeral=True)
		except Exception as e:
			await interaction.followup.send(f"Erreur : {e}", ephemeral=True)

async def setup(bot):
	await bot.add_cog(ClearMessages(bot))
