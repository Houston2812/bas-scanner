# Breach and Attack simulator  
The repository for the scanner of breach and attack simulator tool.     
Scanner - scan engine  
    2.1 To run it set following env variables in docker  
        * SCAN_CATEGORY  
        * SCAN_TYPE  
        * SCAN_SPEED    
    2.2 Create scanner.env file for docker compose that specifies the config for scan. Default config:
        * IS_SET=True  
        * SCAN_TYPE=DIRECTORY_TRAVERSAL_BASIC  
        * SCAN_CATEGORY=DIRECTORY_TRAVERSAL  
        * SCAN_SPEED=SLOW  
