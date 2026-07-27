import discord
from .member import _validate_member_email
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
        try:
            _validate_member_email(self.emailAddress.value,self.firstName.value,self.lastName.value)
        except ValueError as e:
            await interaction.response.send_message(e)
            return

        await interaction.response.send_message('Hi this is email is okay')



@onboarding_group.command(name='input',description='using the first inputmethod')
async def onboarding_input(interaction:discord.Interaction):
    await interaction.response.send_modal(test_modal(   ))
    return