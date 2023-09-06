from azure.identity import DefaultAzureCredential
from azure.mgmt.frontdoor import FrontDoorManagementClient
import sys

subscription_id = '217d2bdc-2706-4aa7-be71-457045f1baba'
resource_group = 'srikali2009'
front_door_name = 'srikali2009fd'
backend_pool_name = 'DefaultBackendPool'

def main(action):
    # Authenticate using the default Azure credentials
    credential = DefaultAzureCredential()
    client = FrontDoorManagementClient(credential, subscription_id)

    # Get the current Front Door configuration
    front_door = client.front_doors.get(resource_group, front_door_name)

    # Get the backend pool
    backend_pool = [pool for pool in front_door.backend_pools if pool.name == backend_pool_name][0]

    if action == '1':
        backend_pool.backends[0].enabled_state = 'Disabled'
        backend_pool.backends[0].weight = 1
        backend_pool.backends[1].enabled_state = 'Enabled'
        backend_pool.backends[1].weight = 100
    elif action == '2':
        backend_pool.backends[0].enabled_state = 'Enabled'
        backend_pool.backends[0].weight = 100
        backend_pool.backends[1].enabled_state = 'Disabled'
        backend_pool.backends[1].weight = 1
    elif action == 'UP':
        backend_pool.backends[0].enabled_state = 'Enabled'
        backend_pool.backends[0].weight = 50
        backend_pool.backends[1].enabled_state = 'Enabled'
        backend_pool.backends[1].weight = 50
    else:
        print('Invalid action:', action)from azure.identity import DefaultAzureCredential
from azure.mgmt.frontdoor import FrontDoorManagementClient
import os
import sys

# Retrieve the environment variables
subscription_id = '217d2bdc-2706-4aa7-be71-457045f1baba'
resource_group = 'srikali2009'
front_door_name = 'srikali2009fd'
backend_pool_name = 'DefaultBackendPool'

def main(action):
    # Authenticate using the default Azure credentials
    credential = DefaultAzureCredential()
    client = FrontDoorManagementClient(credential, subscription_id)

    # Get the current Front Door configuration
    front_door = client.front_doors.get(resource_group, front_door_name)

    # Get the backend pool
    backend_pool = [pool for pool in front_door.backend_pools if pool.name == backend_pool_name][0]

    # Perform the desired action on the backend pool
    # Add your logic here...

    # Update the Front Door configuration
    client.front_doors.begin_create_or_update(resource_group, front_door_name, front_door).result()

    print(f'Action {action} applied successfully.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script.py <action>')
        sys.exit(1)

    main(sys.argv[1])

        return

    # Update the Front Door configuration
    client.front_doors.begin_create_or_update(resource_group, front_door_name, front_door).result()

    print(f'Action {action} applied successfully.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script.py <action>')
        sys.exit(1)

    main(sys.argv[1])
