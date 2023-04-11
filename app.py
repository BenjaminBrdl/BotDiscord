import discord
import asyncio
import datetime

TOKEN = "MTA5NTQ0MjExOTgwMTQ1MDUwNw.GcLk66.Mdmc-x7ov6C7Lxk4BkgQdTJpbpyae1r2-ws3FU"

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    user = await client.fetch_user("Mr2B#9605") # Remplacez "votre_identifiant_discord" par votre propre identifiant Discord

    while not client.is_closed():
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        if hour == minute and minute in [12, 14, 16, 18, 20, 22]:
            await user.send(f"Bonjour ! Il est {hour:02d}:{minute:02d}.")
        await asyncio.sleep(60) # Attendre une minute avant de vérifier à nouveau l'heure

@client.event
async def on_ready():
    print("Le bot est connecté.")

client.loop.create_task(my_background_task())
client.run(TOKEN)
