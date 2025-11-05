import discord
from discord import app_commands
from discord.ext import commands
from .aov_data import add_player, remove_player, update_player_time, get_players
AOV_CHANNEL_ID = 1404094693150687252

class AOV(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_aov_channel(self, interaction):
        return interaction.channel_id == AOV_CHANNEL_ID

    @app_commands.command(name="aov-join", description="Rejoindre la partie Action/Vérité")
    async def aov_join(self, interaction: discord.Interaction):
        if not self.is_aov_channel(interaction):
            await interaction.response.send_message("Commande uniquement utilisable dans le salon Action/Vérité.", ephemeral=True)
            return
        add_player(interaction.guild.id, interaction.user.id)
        await interaction.response.send_message(f"{interaction.user.mention} a rejoint la partie !", ephemeral=True)

    @app_commands.command(name="aov-leave", description="Quitter la partie Action/Vérité")
    async def aov_leave(self, interaction: discord.Interaction):
        if not self.is_aov_channel(interaction):
            await interaction.response.send_message("Commande uniquement utilisable dans le salon Action/Vérité.", ephemeral=True)
            return
        remove_player(interaction.guild.id, interaction.user.id)
        await interaction.response.send_message(f"{interaction.user.mention} a quitté la partie.", ephemeral=True)

    @app_commands.command(name="aov-next", description="Passer le tour d'un joueur")
    @app_commands.describe(member="Le joueur dont le tour doit être passé")
    async def aov_next(self, interaction: discord.Interaction, member: discord.Member):
        if not self.is_aov_channel(interaction):
            await interaction.response.send_message("Commande uniquement utilisable dans le salon Action/Vérité.", ephemeral=True)
            return
        update_player_time(interaction.guild.id, member.id)
        await interaction.response.send_message(f"Le tour de {member.mention} a été mis à jour !", ephemeral=True)

    @app_commands.command(name="aov-last-played", description="Voir le tableau des derniers tours des joueurs")
    async def aov_last_played(self, interaction: discord.Interaction):
        if not self.is_aov_channel(interaction):
            await interaction.response.send_message("Commande uniquement utilisable dans le salon Action/Vérité.", ephemeral=True)
            return
        players = get_players(interaction.guild.id)
        if not players:
            await interaction.response.send_message("Aucun joueur dans la partie.", ephemeral=True)
            return
        # Tri par timecode décroissant
        sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
        lines = []
        import datetime
        for user_id, timestamp in sorted_players:
            member = interaction.guild.get_member(int(user_id))
            mention = member.mention if member else f"<@{user_id}>"
            dt_paris = datetime.datetime.fromtimestamp(timestamp + 7200)
            heure = dt_paris.strftime("%H:%M:%S")
            lines.append(f"{mention} : {heure}")
        table = "\n".join(lines)
        await interaction.response.send_message(f"**Derniers tours des joueurs :**\n{table}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AOV(bot))