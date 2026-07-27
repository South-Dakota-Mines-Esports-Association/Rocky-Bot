import discord
from discord import app_commands

@app_commands.command(name='hello', description='yuh')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('I can do anything!!', ephemeral=True)

