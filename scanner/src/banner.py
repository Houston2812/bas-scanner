from config import SCANNER_DIR, IS_SET, SCAN_CONFIG
from project_logger import logger
from enum import Enum

class ScanConfig():
    def __init__(self, scan_category, scan_type, scan_speed) -> None:
        self.scan_category = scan_category
        self.scan_type = scan_type
        self.scan_speed = scan_speed

    def __repr__(self) -> str:
        return f"Category : {self.scan_category}; Type : {self.scan_type}; Speed : {self.scan_speed}"

class Speeds(Enum):
    SLOW = 5
    NORMAL = 3
    FAST = 1 

Payloads = {
    "DIRECTORY_TRAVERSAL": {
        "DIRECTORY_TRAVERSAL_FULL" : f"{SCANNER_DIR}/payloads/directory_traversal/directory_traversal.md",
        "DIRECTORY_TRAVERSAL_BASIC" : f"{SCANNER_DIR}/payloads/directory_traversal/directory_traversal_basic.md",
        "DIRECTORY_TRAVERSAL_SHORT" : f"{SCANNER_DIR}/payloads/directory_traversal/directory_traversal_short.md"
    },
    "SQL_INJECTION": {
        "SQL_INJECTION_FULL" : f"{SCANNER_DIR}/payloads/sql_injection/sql_injection.md"
    }
}

def create_config(scan_category, scan_type, scan_speed):
    return ScanConfig(scan_category=scan_category, scan_type=Payloads[scan_category][scan_type], scan_speed=Speeds[scan_speed])

def scan_banner():
    if IS_SET == True:
        # if scan_speed == 1:
        #     scan_speed = Speeds['SLOW']
        # elif scan_speed == 2:
        #     scan_speed = Speeds['NORMAL']
        # elif scan_speed == 3:
        #     scan_speed = Speeds['FAST']
        logger.debug("ENV VAR RECEIVED")
        return ScanConfig(scan_category=SCAN_CONFIG['SCAN_CATEGORY'], scan_type=Payloads[SCAN_CONFIG['SCAN_CATEGORY']][SCAN_CONFIG['SCAN_TYPE']], scan_speed=Speeds[SCAN_CONFIG['SCAN_SPEED']])

    print("Select the scan category:")
    print("\t[1] Directory Traversal")
    print("\t[2] SQL Injection")
    print()

    scan_category = int(input("Category: "))

    if scan_category == 1:
        index = 1
        scan_category = "DIRECTORY_TRAVERSAL"
        print("Select scan type for Directory Traversal:")
        for key in Payloads["DIRECTORY_TRAVERSAL"].keys():
            print(f"\t[{index}] {key}")
            index = index + 1
        print()

    elif scan_category == 2:
        index = 1
        scan_category = "SQL_INJECTION"
        print("Select scan type for SQL Injection:")
        for key in Payloads["SQL_INJECTION"].keys():
            print(f"\t[{index}] {key}")
            index = index + 1

    scan_type = int(input("Type: "))
    
    print("Select the scan speed:")
    print("\t[1] SLOW")
    print("\t[2] NORMAL")
    print("\t[2] FAST")
    print()

    scan_speed = int(input("Speed: "))
    
    if scan_speed == 1:
        scan_speed = Speeds['SLOW']
    elif scan_speed == 2:
        scan_speed = Speeds['NORMAL']
    elif scan_speed == 3:
        scan_speed = Speeds['FAST']
    
    return ScanConfig(scan_category=scan_category, scan_type=Payloads[scan_category][list(Payloads[scan_category])[scan_type-1]], scan_speed=scan_speed)
