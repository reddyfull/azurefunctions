import os
import json
from azure.identity import DefaultAzureCredential
from azure.appconfiguration import AzureAppConfigurationClient

# Azure App Configuration details
connection_string = os.getenv('APP_CONFIGURATION_ACCESS_KEY')

# Parse the JSON file
with open('test_appsettings.json', 'r') as f:
    data = json.load(f)

# Initialize the Azure App Configuration client
client = AzureAppConfigurationClient.from_connection_string(connection_string)

# Iterate over the items in the JSON file and add them to Azure App Configuration
for key, value in data.items():
    client.set_configuration_setting(key, value)
