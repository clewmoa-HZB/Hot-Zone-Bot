async def log_suppression(message_type, message_id, user_id, bot=None):
	if bot is None:
		return
	channel = bot.get_channel(LOG_CHANNEL_ID)
	if not channel:
		return
	embed = discord.Embed(title=f"Suppression de {message_type}", description=f"Message ID : {message_id}", color=discord.Color.red())
	embed.add_field(name="Auteur de la suppression", value=str(user_id), inline=False)
	await channel.send(embed=embed)
import discord
LOG_CHANNEL_ID = 1409259784946978847

async def log_confession(confession_num, msg_url, user_id, contenu, image_url=None, bot=None):
	if bot is None:
		return
	channel = bot.get_channel(LOG_CHANNEL_ID)
	if not channel:
		return
	embed = discord.Embed(title=f"Log Confession n°{confession_num}", description=contenu, color=discord.Color.blue())
	embed.add_field(name="Auteur", value=str(user_id), inline=False)
	embed.add_field(name="Lien du message", value=msg_url, inline=False)
	if image_url:
		embed.set_image(url=image_url)
	await channel.send(embed=embed)

async def log_reponse(confession_num, reponse_num, msg_url, user_id, contenu, image_url=None, bot=None):
	# Cette fonction doit être appelée avec le bot Discord
	if bot is None:
		# Impossible d'envoyer le log sans le bot
		return
	channel = bot.get_channel(LOG_CHANNEL_ID)
	if not channel:
		return
	embed = discord.Embed(title=f"Log Réponse à la confession {confession_num} n°{reponse_num}", description=contenu, color=discord.Color.orange())
	embed.add_field(name="Auteur", value=str(user_id), inline=False)
	embed.add_field(name="Lien du message", value=msg_url, inline=False)
	if image_url:
		embed.set_image(url=image_url)
	await channel.send(embed=embed)
