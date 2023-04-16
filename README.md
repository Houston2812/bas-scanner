# Breach and Attack simulator  
The repository for the scanner of breach and attack simulator tool.       
Scanner - scan engine  

1. To run it set following env variables in docker   
        1.1 SCAN_CATEGORY    
        1.2 SCAN_TYPE    
        1.3 SCAN_SPEED      
2. Create scanner.env file for docker compose that specifies the config for scan. Default config:  
        2.1 IS_SET=True     
        2.2 SCAN_TYPE=DIRECTORY_TRAVERSAL_BASIC    
        2.3 SCAN_CATEGORY=DIRECTORY_TRAVERSAL    
        2.4 SCAN_SPEED=SLOW    
