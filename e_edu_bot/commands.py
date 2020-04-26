import discord

allowed_roles = []


async def command_help(client, message: discord.message.Message):
    await message.channel.send("Für die Rolle Watcher klicke auf die 👀!")


async def send_welcome_message_id(client, message):
    msg = """
Hey! Willkommen auf dem E-Edu-Server :slight_smile:
Hier gibt es Verschiedene Aufgabengebiete. 
Im #infos Channel findest du mehr Infos zu allen Bereichen.

Wenn du dich entschieden hast wo du gerne mal 
reinschauen oder gar mitmachen möchtest dann 
klicke bitte eine der folgenden Zahlen / Emojis an :slight_smile:
Es wird durch anklicken einer Zahl, eine Anfrage an die Heads des jeweiligen Bereichs gesendet.

1 » Frontend
2 » Schnittstellen
3 » User Microservice
4 » Report Microservice
5 » Task MicroService
6 » Design
👀 » Watcher
"""

    a = await message.channel.send(msg)
    for i in ["1️⃣", '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '👀']:
        await a.add_reaction(i)
    client.edu_config.update_value("request_permission_message", str(a.id))


async def handle_admin_command(client, message: discord.message.Message):
    if client.edu_config.old_user_admin is not None:
        if str(message.author) == str(client.edu_config.old_user_admin):
            await message.author.send_message("Die Config File wurde aktualisiert!")
            admin_id = message.author.id
            client.edu_config.admin_client_list.append(int(admin_id))
            client.edu_config.remove_old_key("admin_client")
            client.edu_config.update_value(
                "admin_client_list", client.edu_config.admin_client_list)
            client.edu_config.old_user_admin = None
    if not int(message.author.id) in client.edu_config.admin_client_list:
        await message.add_reaction('⚠️')
        return

    full_message = message.content.split(" ")
    if len(full_message) <= 1:
        await message.add_reaction('❓')
        return
    if full_message[1] == "register_welcome_channel":
        await send_welcome_message_id(client, message)
    elif full_message[1] == "register_frontend_bot_channel":
        client.edu_config.update_value(
            "frontend_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')
    elif full_message[1] == "register_interface_bot_channel":
        client.edu_config.update_value(
            "interface_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')
    elif full_message[1] == "register_user_bot_channel":
        client.edu_config.update_value(
            "user_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')
    elif full_message[1] == "register_report_bot_channel":
        client.edu_config.update_value(
            "report_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')
    elif full_message[1] == "register_task_bot_channel":
        client.edu_config.update_value(
            "task_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')
    elif full_message[1] == "register_design_bot_channel":
        client.edu_config.update_value(
            "design_bot_channel", str(message.channel.id))
        await message.add_reaction('👍')

    elif full_message[1] == "register_admin":
        admin_id = full_message[2]
        client.edu_config.admin_client_list.append(int(admin_id))
        client.edu_config.update_value(
            "admin_client_list", client.edu_config.admin_client_list)
        await message.add_reaction('👍')

    elif full_message[1] == "get_owner_info":
        await message.author.send(str(await client.application_info()))
        await message.add_reaction('👍')
    else:
        await message.add_reaction('❓')


async def handle_role_remove_command(client, message):
    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name=message.content[2:].strip()))
