import discord

allowed_roles = []


async def command_help(client, message: discord.message.Message):
    # Todo New Help
    await message.channel.send("Für die Rolle Watcher tippe .+ Watcher")


async def send_welcome_message_id(client, message):
    a = await message.channel.send(
        "Wilkommen auf dem Discord Server!\n Reagier mit dem passendem Emoji, um einem Team beitreten zu können!")

    for i in ["1️⃣", '2️⃣', '3️⃣', '4️⃣', '5️⃣']:
        await a.add_reaction(i)
    client.edu_config.update_value("request_permission_message", str(a.id))


async def handle_admin_command(client, message: discord.message.Message):
    if str(message.author) is str(client.edu_config.admin_client):
        return
    full_message = message.content.split(" ")
    if len(full_message) < 1:
        return
    if full_message[1] == "register_welcome_channel":
        await send_welcome_message_id(client, message)


    elif full_message[1] == "register_frontend_bot_channel":
        client.edu_config.update_value("frontend_bot_channel", str(message.channel.id))

    elif full_message[1] == "register_interface_bot_channel":
        client.edu_config.update_value("interface_bot_channel", str(message.channel.id))

    elif full_message[1] == "register_user_bot_channel":
        client.edu_config.update_value("user_bot_channel", str(message.channel.id))

    elif full_message[1] == "register_report_bot_channel":
        client.edu_config.update_value("report_bot_channel", str(message.channel.id))

    elif full_message[1] == "register_task_bot_channel":
        client.edu_config.update_value("task_bot_channel", str(message.channel.id))
    else:
        return  # Todo Not Found
