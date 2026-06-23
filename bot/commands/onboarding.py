import discord
from discord import app_commands
from discord import ui

onboarding_group = app_commands.Group(name='onboarding', description='blablahtest - charlie')

class test_modal(ui.Modal, title='test input 2'):
    name = ui.TextInput(label='shit')

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)

@onboarding_group.command(name='inputmethod1',description='using the first inputmethod')
async def inputmethod1(self, interaction:discord.Interaction):
    await interaction.response.send_modal(test_modal(   ))
    return