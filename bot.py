import os
from e_edu_bot import EEduBot
import threading

token = os.environ.get("DISCORD_TOKEN")

if token is None or len(token) < 5:
    raise Exception("Discord Token is not valid")

client = EEduBot()

thread = threading.Thread(target=client.reset_cooldown)
thread.daemon = True
thread.start()

client.run(token)
