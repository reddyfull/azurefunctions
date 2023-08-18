#!/bin/bash

# Resource group and Front Door name
resourceGroup="srikali2009"
frontDoorName="srikali2009fd"

# Backend pools
backends=(
  "srikali2009.azurewebsites.net"
  "srikalistage2009.azurewebsites.net"
)

# Create the Front Door
az network front-door create \
  --resource-group $resourceGroup \
  --name $frontDoorName \
  --backend-address $backends

# Create routing rules (modify as needed)
for backend in "${backends[@]}"; do
  az network front-door routing-rule create \
    --resource-group $resourceGroup \
    --front-door-name $frontDoorName \
    --name "${backend}-rule" \
    --frontend-endpoints "default" \
    --route-type Forward \
    --backend-pool DefaultBackendPool
done