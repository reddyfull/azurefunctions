#!/bin/bash

resourceGroup="srikali2009"
frontDoorName="srikali2009fd"

# Define the backends
backends=(
  "srikali2009.azurewebsites.net"
  "srikalistage2009.azurewebsites.net"
)

# Get the active backend
activeBackend=$1

# Determine the status of the backends
if [ "$activeBackend" == "1" ]; then
  enabled1=true
  enabled2=false
elif [ "$activeBackend" == "2" ]; then
  enabled1=false
  enabled2=true
elif [ "$activeBackend" == "UP" ]; then
  enabled1=true
  enabled2=true
else
  echo "Invalid active backend"
  exit 1
fi

# Update the status of the backends
az network front-door backend-pool backend update \
  --resource-group $resourceGroup \
  --front-door-name $frontDoorName \
  --pool-name DefaultBackendPool \
  --address "${backends[0]}" \
  --index 1 \
  --enabled $enabled1

az network front-door backend-pool backend update \
  --resource-group $resourceGroup \
  --front-door-name $frontDoorName \
  --pool-name DefaultBackendPool \
  --address "${backends[1]}" \
  --index 2 \
  --enabled $enabled2