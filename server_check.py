import discord

def server_check():
	def is_guild_allowed(guild_id):
		allowed_guilds = [1391083075424747660]
		return guild_id in allowed_guilds

	return is_guild_allowed