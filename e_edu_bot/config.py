import json
import os


class Config:
    config_file_path = "./config/config.json"
    user_id_file_path = "./config/user_id.json"
    config_folder_path = "./config"

    # see config.json
    old_user_admin = None

    admin_client_list = None
    request_permission_message = None
    frontend_bot_channel = None
    interface_bot_channel = None
    user_bot_channel = None
    report_bot_channel = None
    task_bot_channel = None
    design_bot_channel = None
    timeout_list = []
    # The name of the roles are defined in the 'update_channel_list' function
    user_id_dic = {}
    defaultConfig = {
        "admin_client_list": [],
        "_": "Don't touch the stuff below. this will be generated by the bot!",
        "__": "If you delete the Channel, you need to reconfigure the bot with the .admin command!",
        "request_permission_message": "",

        "frontend_bot_channel": "",
        "interface_bot_channel": "",
        "user_bot_channel": "",
        "report_bot_channel": "",
        "task_bot_channel": "",
        "design_bot_channel": ""
    }

    permission_name_list = {}

    def __init__(self):
        self.validate_config_file()
        self.read_config()
        self.read_user_dict_file()

    def read_config(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as f:
                data = f.read()
            json_data = json.loads(data)

            self.frontend_bot_channel = json_data["frontend_bot_channel"]
            self.interface_bot_channel = json_data["interface_bot_channel"]
            self.user_bot_channel = json_data["user_bot_channel"]
            self.report_bot_channel = json_data["report_bot_channel"]
            self.task_bot_channel = json_data["task_bot_channel"]
            self.request_permission_message = json_data["request_permission_message"]
            self.design_bot_channel = json_data["design_bot_channel"]
            self.admin_client_list = json_data["admin_client_list"]

            if "admin_client" in json_data:
                self.old_user_admin = json_data["admin_client"]
            self.update_channel_list()
        else:
            self.create_default_config_file()

    def update_channel_list(self):
        for i in [
            [self.frontend_bot_channel, "Frontend"],
            [self.interface_bot_channel, "Schnittstellen"],
            [self.user_bot_channel, "User Ms"],
            [self.report_bot_channel, "Report Ms"],
            [self.task_bot_channel, "Task MS"],
            [self.design_bot_channel, "Design"]
        ]:
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

    def validate_config_file(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as f:
                data = f.read()
            json_data = json.loads(data)

            for i in self.defaultConfig:
                if not i in json_data:
                    json_data[i] = self.defaultConfig[i]

            with open(self.config_file_path, 'w') as f:
                json.dump(json_data, f)

    def remove_old_key(self, key):
        with open(self.config_file_path, 'r') as f:
            data = f.read()
        json_data = json.loads(data)

        json_data.pop(key)

        with open(self.config_file_path, 'w') as f:
            json.dump(json_data, f)
