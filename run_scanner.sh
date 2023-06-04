#!/bin/bash

echo "Running scanner"

read -p "Enter the Authentication key: " auth_key

echo "Authentication key: $auth_key"

touch scanner/key.env 
echo "KEY=$auth_key" > scanner/key.env 

docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest

docker-compose -f ./scanner/docker-compose.yml up 
