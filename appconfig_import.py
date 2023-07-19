import json
import subprocess
import os

def import_config():
    with open('./test_appsettings.json') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            subprocess.run(["az", "appconfig", "kv", "set", "--name", os.environ['CONFIGURATION_STORE_NAME'], "--key", key, "--value", value, "--connection-string", os.environ['APP_CONFIGURATION_ACCESS_KEY']])

if __name__ == "__main__":
    import_config()
