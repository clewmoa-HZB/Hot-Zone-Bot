import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv("BOT_TOKEN")
nsfw_key = os.getenv("API_NSFW_Bot")

print(f"Token loaded: {'Yes' if token else 'No'}")
print(f"API NSFW Key loaded: {'Yes' if nsfw_key else 'No'}")

if not token:
    raise ValueError("Token not found in .env")
if not nsfw_key:
    raise ValueError("API_NSFW_Bot not found in .env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

import cogs

async def update_presence(bot):
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Mise à jour terminée"
        ),
        status=discord.Status.online
    )
    print("Discord Rich Presence mise à jour avec succès.")

@bot.event
async def on_ready():
    print(f"Connecté en tant que : {bot.user}")
    await update_presence(bot)

async def main():
    cogs.setup_cogs(bot)
    await bot.start(token)

@bot.event
async def on_ready():
    print(f"Connecté en tant que : {bot.user}")
    print("Liste des serveurs :")
    for guild in bot.guilds:
        try:
            owner = guild.owner
            print(f"- {guild.name} (ID: {guild.id}) | Fondateur: {owner} (ID: {owner.id})")
        except Exception as e:
            print(f"Erreur lors de la récupération du propriétaire du serveur {guild.name}: {e}")
    await update_presence(bot)

    # Envoi de l'embed dans le salon spécifié
    channel_id = 1409928624735391785
    channel = bot.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title="Log de haute importance",
            description="Mise à jour du bot en cours, plusieurs redémarrages peuvent avoir lieu.",
            color=discord.Color.red()
        )
        await channel.send(embed=embed)
    else:
        print(f"Salon avec l'ID {channel_id} introuvable.")

if __name__ == "__main__":
    try:
        print("Démarrage du bot...")
        asyncio.run(main())
    except Exception as e:
        print(f"Erreur lors du démarrage du bot : {e}")