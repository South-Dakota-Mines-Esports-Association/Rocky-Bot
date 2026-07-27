import discord
from discord import app_commands
from discord import ui

onboarding_group = app_commands.Group(
    name='onboarding', 
    description='blablahtest - charlie'
)

class test_modal(ui.Modal, title='test input 2'):
    firstName = ui.TextInput(label='First Name')
    lastName = ui.TextInput(label='Last Name')
    emailAddress = ui.TextInput(label='Email Address')
    classStanding = ui.TextInput(label='Class Standing')

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
        await interaction.followup.send(f'Here is your data {self.firstName}, {self.lastName}, {self.emailAddress}, {self.classStanding}')

@onboarding_group.command(name='input',description='using the first inputmethod')
async def onboarding_input(interaction:discord.Interaction):
    await interaction.response.send_modal(test_modal(   ))
    return