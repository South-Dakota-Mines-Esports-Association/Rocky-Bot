import discord
from .member import _validate_member_email
from discord import app_commands
from discord import ui

from bot.commands.common import (
    ACADEMIC_YEAR_CHOICES,
    ApiPayloadModal,
    ModalField,
    clean_payload,
    execute_api_command,
    optional_choice,
    optional_text,
    require_choice,
    require_payload,
    require_positive_int,
    require_positive_int_text,
    require_text,
    send_validation_error,
)

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

        result = execute_api_command(
            interaction,
            'Test',
            'POST',
            '/member',
            params={},
            request_body = {
                'first_name' : self.firstName.value, 
                'last_name' : self.lastName.value, 
                'email_address' : self.emailAddress.value
            }
        )

        await interaction.response.send_message(result)
        



@onboarding_group.command(name='input',description='using the first inputmethod')
async def onboarding_input(interaction:discord.Interaction):
    await interaction.response.send_modal(test_modal(   ))
    return