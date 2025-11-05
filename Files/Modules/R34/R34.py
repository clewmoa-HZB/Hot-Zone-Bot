import discord
from discord import app_commands
from discord.ext import commands
import random
import os

# Dummy function for server check (to be replaced by actual import)
def is_guild_allowed(interaction):
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
    from server_check import server_check
    return server_check(interaction.guild.id)

class R34(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="r34", description="Recherche une image R34 avec tags obligatoires et facultatifs.")
    @app_commands.describe(
        tag1="Tag obligatoire 1",
        tag2="Tag obligatoire 2",
        tag3="Tag obligatoire 3",
        tag4="Tag obligatoire 4",
        tag5="Tag obligatoire 5",
        opt1="Tag facultatif 1 (optionnel)",
        opt2="Tag facultatif 2 (optionnel)",
        opt3="Tag facultatif 3 (optionnel)"
    )
    async def r34(self, interaction: discord.Interaction, tag1: str, tag2: str = None, tag3: str = None, tag4: str = None, tag5: str = None, opt1: str = None, opt2: str = None, opt3: str = None):
        if not is_guild_allowed(interaction):
            await interaction.response.send_message("Commande non autorisée sur ce serveur.", ephemeral=True)
            return
        # Simulation de recherche d'image (à remplacer par l'appel API réel)
        tags = [tag1, tag2, tag3, tag4, tag5]
        optional = [opt1, opt2, opt3]
        # Ici, on simule une image trouvée
        all_tags = [t for t in tags + optional if t]
        tag_string = "+".join(all_tags)
        image_url = f"https://rule34.xxx/index.php?page=post&s=list&tags={tag_string}"
        await interaction.response.send_message(f"{image_url}")

async def setup(bot):
    await bot.add_cog(R34(bot))
