# Scanner of BAS
This is the scanner of Breach and Attack Simulation tool.  
Scanner is the dockerized application that run using docker-compose in the daemon mode.

## Tech stack
The scanner is written using following technologies:
* Python - Requests, redis, logger
* Redis - used to perform in memory storage. It was choosen due to the high performance, as the data is stored in the database of interface it could be deleted from the logs of scanner. 
* Payloads - currently there are payloads for Directory Traversal, SQL Injection, XSS

## Flow
To start a scan following actions should be performed:
* Run the scanner in the same subnet as sensor
* The script will promt user for the authentication key, that is syncronized with the interface. It will run only if the correct key is provided. 
* When user will queue new scan, the scanner will receive this information and will start the execution.
* In the end the results will be composed in the instance of Report class and sent to the user interface, as well as shown in the CLI.

## Set-up
To set up the application perform following operations:  
* Pull the project from the git
* Execute the launch script
        * ./run_scanner.sh
* Provide the authentication key to the prompt

