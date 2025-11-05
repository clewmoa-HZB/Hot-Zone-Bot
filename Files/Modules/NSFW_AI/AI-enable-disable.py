import discord
from discord import app_commands
from discord.ext import commands
import yaml
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../../Data/NSFW_AI/status.yaml')

def load_status():
    if not os.path.exists(DATA_PATH):
        return {'enabled': [], 'disabled': []}
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {'enabled': [], 'disabled': []}

def save_status(status):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        yaml.safe_dump(status, f)

def update_status(channel_id, enable=True):
    status = load_status()
    if enable:
        if channel_id in status['disabled']:
            status['disabled'].remove(channel_id)
        if channel_id not in status['enabled']:
            status['enabled'].append(channel_id)
    else:
        if channel_id in status['enabled']:
            status['enabled'].remove(channel_id)
        if channel_id not in status['disabled']:
            status['disabled'].append(channel_id)
    save_status(status)

def is_guild_allowed(interaction):
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
    from server_check import server_check
    return server_check(interaction.guild.id)

class NSFWAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="nsfw-ai-enable", description="Activer l'IA NSFW dans un salon.")
    @app_commands.describe(channel="Salon à activer (optionnel)")
    async def nsfw_ai_enable(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        if not is_guild_allowed(interaction):
            await interaction.response.send_message("Commande non autorisée sur ce serveur.", ephemeral=True)
            return
        channel = channel or interaction.channel
        update_status(channel.id, enable=True)
        await interaction.response.send_message(f"IA NSFW activée dans {channel.mention}", ephemeral=True)

    @app_commands.command(name="nsfw-ai-disable", description="Désactiver l'IA NSFW dans un salon.")
    @app_commands.describe(channel="Salon à désactiver (optionnel)")
    async def nsfw_ai_disable(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        if not is_guild_allowed(interaction):
            await interaction.response.send_message("Commande non autorisée sur ce serveur.", ephemeral=True)
            return
        channel = channel or interaction.channel
        update_status(channel.id, enable=False)
        await interaction.response.send_message(f"IA NSFW désactivée dans {channel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(NSFWAI(bot))
