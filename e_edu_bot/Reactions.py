import discord


async def handle_bool_emoji(client, payload: discord.raw_models.RawReactionActionEvent):
    if str(payload.emoji) == "✅":
        role_name = client.edu_config.permission_name_list[str(payload.channel_id)]
        role = discord.utils.get(payload.member.guild.roles, name=role_name)

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        username = message.content.split(" ")[0]

        guild = client.get_guild(payload.guild_id)
        user = guild.get_member(client.edu_config.user_id_dic[str(username)])
        await user.add_roles(role)
        await user.remove_roles(discord.utils.get(payload.member.guild.roles, name="Watcher"))
        await message.delete()

        permitted_user = guild.get_member(payload.user_id)
        await channel.send("Der User " + str(username) + " wurde von " + str(
            permitted_user) + " zur Gruppe " + role_name + " hinzugefügt")
    elif str(payload.emoji) == "❌":
        role_name = client.edu_config.permission_name_list[str(payload.channel_id)]
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        username = message.content.split(" ")[0]
        permitted_user = client.get_guild(payload.guild_id).get_member(payload.user_id)
        await message.delete()

        await client.get_channel(payload.channel_id).send(
            "Der Nutzer " + username + " wurde aufgrund der Entscheidung von " + str(
                permitted_user) + " nicht zur Gruppe hinzugefügt")
        await client.get_guild(payload.guild_id).get_member(client.edu_config.user_id_dic[str(username)]).send(
            "Du wurdest aufgrund der Entscheidung von " + str(
                permitted_user) + ' nicht zur Gruppe "' + role_name + '" hinzugefügt')


async def handle_request_group_emoji(client, payload: discord.raw_models.RawReactionActionEvent):
    if payload.user_id in client.edu_config.timeout_list:
        return
    else:
        client.edu_config.timeout_list.append(payload.user_id)
    user = client.get_user(payload.user_id)
    if str(payload.emoji) == "1️⃣":
        channel_id = client.edu_config.frontend_bot_channel
    elif str(payload.emoji) == '2️⃣':
        channel_id = client.edu_config.report_bot_channel
        print(client.edu_config.report_bot_channel)
    elif str(payload.emoji) == '3️⃣':
        channel_id = client.edu_config.interface_bot_channel
    elif str(payload.emoji) == '4️⃣':
        channel_id = client.edu_config.task_bot_channel
    elif str(payload.emoji) == "5️⃣":
        channel_id = client.edu_config.user_bot_channel
    elif str(payload.emoji) == '6️⃣':
        channel_id = client.edu_config.design_bot_channel
    elif str(payload.emoji) == '7️⃣':
        await client.get_guild(payload.guild_id).get_member(payload.user_id).add_roles(
            discord.utils.get(payload.member.guild.roles, name="Watcher"))
        return
    else:
        return

    channel = client.get_channel(int(channel_id))
    client.edu_config.save_user_context(str(payload.member), payload.user_id)
    m = await channel.send("@" + str(
        user) + " möchte dem Team beitreten! \n Warnung! Wenn der Emoji von der nachricht entfernt wird, behält der Nutzer weiterhin die Rolle")

    for i in ["✅", "❌"]:
        await m.add_reaction(i)
