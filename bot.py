import discord



SALON_LOGS_ID = 1498890074601951282
SALON_RECAP_ID = 1499222076693676193
RR_TRACKER_ID = 1220016509888364608

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author.id != RR_TRACKER_ID:
        return

    if message.channel.id != SALON_LOGS_ID:
        return

    if message.embeds:
        embed = message.embeds[0]

        if embed.title and "Récapitulatif de la veille" in embed.title:
            channel = client.get_channel(SALON_RECAP_ID)
            await channel.send(embed=embed)

import os
client.run(os.getenv("TOKEN"))
