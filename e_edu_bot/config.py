import json
import os


class Config:
    config_file_path = "./config/config.json"
    user_id_file_path = "./config/user_id.json"
    config_folder_path = "./config"
    admin_client = None
    request_permission_message = None

    frontend_bot_channel = None
    interface_bot_channel = None
    user_bot_channel = None
    report_bot_channel = None
    task_bot_channel = None
    design_bot_channel = None
    timeout_list = []

    ms_channel_list = []
    user_id_dic = {}
    defaultConfig = {
        "admin_client": "DevMax#4016",

        "request_permission_message": "",
        "frontend_bot_channel": "",
        "interface_bot_channel": "",
        "user_bot_channel": "",
        "report_bot_channel": "",
        "task_bot_channel": "",
        "design_bot_channel":""
    }

    permission_name_list = {}

    def __init__(self):
        self.read_config()
        self.read_user_dict_file()

    def read_config(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as f:
                data = f.read()
            json_data = json.loads(data)

            self.admin_client = json_data["admin_client"]

            self.frontend_bot_channel = json_data["frontend_bot_channel"]
            self.interface_bot_channel = json_data["interface_bot_channel"]
            self.user_bot_channel = json_data["user_bot_channel"]
            self.report_bot_channel = json_data["report_bot_channel"]
            self.task_bot_channel = json_data["task_bot_channel"]
            self.request_permission_message = json_data["request_permission_message"]
            self.design_bot_channel = json_data["design_bot_channel"]

            self.update_channel_list()
        else:
            self.create_default_config_file()

    def update_channel_list(self):
        self.ms_channel_list = [
            self.frontend_bot_channel,
            self.interface_bot_channel,
            self.user_bot_channel,
            self.report_bot_channel,
            self.task_bot_channel,
            self.design_bot_channel
        ]
        for i in [
            [self.frontend_bot_channel, "Frontend"],
            [self.interface_bot_channel, "Schnittstellen"],
            [self.user_bot_channel, "USER MS"],
            [self.report_bot_channel, "REPORT MS"],
            [self.task_bot_channel, "TASK MS"],
            [self.design_bot_channel, "Design"]]:
            self.permission_name_list[i[0]] = i[1]

    def create_default_config_file(self):
        if not os.path.exists(self.config_folder_path):
            os.mkdir(self.config_folder_path)
        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'w') as f:
                json.dump(self.defaultConfig, f)
                f.flush()
                f.close()
        if not os.path.exists(self.user_id_file_path):
            with open(self.user_id_file_path, 'w') as f:
                json.dump({}, f)
                f.flush()
                f.close()

    def update_value(self, param, value):
        with open(self.config_file_path, 'r') as f:
            data = f.read()
            f.close()
        json_data = json.loads(data)
        json_data[param] = value

        with open(self.config_file_path, 'w') as f:
            json.dump(json_data, f)

        self.read_config()
        print("Reload Done")

    def save_user_context(self, user_name, user_id):
        self.user_id_dic[user_name] = user_id
        with open(self.user_id_file_path, 'w') as f:
            json.dump(self.user_id_dic, f)

    def read_user_dict_file(self):
        if not os.path.exists(self.user_id_file_path):
            self.create_default_config_file()
        with open(self.user_id_file_path, 'r') as f:
            data = f.read()
            f.close()
        json_data = json.loads(data)
        self.user_id_dic = json_data

    def remove_user_dict_key(self, key):
        json_data = self.user_id_dic
        json_data.pop(key)
        with open(self.user_id_file_path, 'w') as f:
            json.dump(json_data, f)
