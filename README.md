
# Python Flask Report Microservice

View **[Dockerfile](https://github.com/E-Edu/discord-bot/blob/master/Dockerfile)** on GitHub.

## Docker image tags

* **Image name:** `eedu/discord`


## Environment Variables

| Variable         | Required | Default   | Description |
|------------------|----------|-----------| ------------|
| `DISCORD_TOKEN` |Yes|  | / |

##available commands

.admin [params]

| Parameter        | Description |
|------------------| ------------|
| `register_welcome_channel`        |save welcome channel id|
| `register_frontend_bot_channel`   |save frontend channel id|
| `register_interface_bot_channel`  |save interface channel id|
| `register_user_bot_channel`       |save user channel id|
| `register_report_bot_channel`     |save report channel id|
| `register_task_bot_channel`       |save task channel id|
| `register_design_bot_channel`     |save design channel id|

.help


### Run with Docker

```bash
docker run \
  -e DISCORD_TOKEN='' \
  eedu/discord
```

### Run with docker-compose

For easy usage, there is a Docker Compose example project included.
```bash
docker-compose up -d
```



