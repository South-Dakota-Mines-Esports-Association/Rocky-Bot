import discord
from discord import app_commands

@app_commands.command(name='goodbye', description='nuh')
async def goodbye(interaction: discord.Interaction):
    await interaction.response.send_message('I cant do anything!!', ephemeral=True)

