import discord

allowed_roles = []


async def command_help(client, message: discord.message.Message):
    # Todo New Help
    await message.channel.send("Für die Rolle Watcher tippe .+ Watcher #frontend")


async def send_welcome_message_id(client, message):
    text_channel = client.get_channel('1234567890')

    msg = """
Hey! Willkommen auf dem E-Edu-Server :slight_smile:
Hier gibt es Verschiedene Aufgabengebiete. 
Im #infos Channel findest du mehr Infos zu allen Bereichen.

Wenn du dich entschieden hast wo du gerne mal 
reinschauen oder gar mitmachen möchtest dann 
klicke bitte eine der folgenden Zahlen an :slight_smile:

1 » Frontend
2 » Design
3 » Schnittstellen
4 » User Microservice
5 » Report Microservice
6 » Task MicroService
7 » Watcher
"""

    a = await message.channel.send(msg)

    for i in ["1️⃣", '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣']:
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
    elif full_message[1] == "register_design_bot_channel":
        client.edu_config.update_value("design_bot_channel", str(message.channel.id))
    else:
        return
