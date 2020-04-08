import time

from .Commands import *
from .config import Config
from .Reactions import *


class EEduBot(discord.Client):
    edu_config = None

    def __init__(self, **options):
        self.edu_config = Config()
        super().__init__(**options)

    async def on_ready(self):
        print("Bot ist online!")

    async def on_message(self, message: discord.message.Message):
        if message.author == self.user:
            return

        if message.content.startswith("."):
            if message.content.startswith(".help"):
                await command_help(self, message)
            elif message.content.startswith(".admin"):
                await handle_admin_command(self, message)

            else:
                await message.channel.send(
                    f"{message.author.mention} Befehl nicht gefunden!")

    async def on_raw_reaction_add(self, payload):
        if payload.member == self.user:
            return
        if str(payload.message_id) == str(self.edu_config.request_permission_message):
            await handle_request_group_emoji(self, payload)

        elif str(payload.channel_id) in self.edu_config.ms_channel_list:
            await handle_bool_emoji(self, payload)

    def reset_cooldown(self):
        while True:
            time.sleep(300)
            self.edu_config.timeout_list = []

