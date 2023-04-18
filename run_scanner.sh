#!/bin/bash

echo "Running scanner"

read -p "Enter the Authorization key: " auth_key

echo "Authorization key: $auth_key"

touch scanner/key.env 
echo "KEY=$auth_key" > scanner/key.env 

# docker run -d --network host redislabs/redismod

#sleep(10) 

docker-compose -f ./scanner/docker-compose.yml up 
