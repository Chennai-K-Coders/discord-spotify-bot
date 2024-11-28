import discord
from discord import app_commands
from discord.ext import commands
from typing import Literal

import os
from dotenv import load_dotenv

from spotify import sp_client_scope




load_dotenv()
GUILD_ID = discord.Object(id=os.getenv("DISCORD_GUILD_ID"))

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {client.user} (ID: {client.user.id})')
        print('---------------')
        
        # Only for dev and test env comment out in prod
        try:
            guild = GUILD_ID
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to the server')
        except Exception as e:
            print(f'Error syncing commands: {e}')


intents = discord.Intents.default()
intents.message_content= True

client = Client(command_prefix="!",intents=intents)

@client.tree.command(guild=GUILD_ID) 
@app_commands.describe(pl_name='playlist name')
@app_commands.describe(no_of_tracks='No of tracks')
async def music_bot_create_pl(interaction: discord.Interaction,no_of_tracks: int,pl_name: str):
    await interaction.response.send_message(content="WORK IN PROGRESS",ephemeral=True)

@client.tree.command(guild=GUILD_ID)
@app_commands.describe(song_name='Song_name')
@app_commands.describe(platform='music platform')
async def music_embed(interaction: discord.Interaction,song_name: str,platform: Literal['Spotify']):
    result = ''
    if platform == 'Spotify':
        sp = sp_client_scope()
        search_result = sp.search(song_name, type ='track')
        result = search_result['tracks']['items'][0]['external_urls']['spotify']
        print(result)
    await interaction.response.send_message(content=result,ephemeral=False)



client.run(os.getenv("DISCORD_BOT_TOKEN"))
