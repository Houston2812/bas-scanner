from project_logger import logger
from config import test_redis
from report import ScanReport
from payload import PayloadPackage
from server import verify_key, check_scan, send_report
from banner import scan_banner, create_config

import time


def read_payloads(file):
    payloads = []
    with open(file, "r") as f:
        logger.warning(f"Reading {file}")

        data = f.readlines()
        counter = 0

        for payload in data:
            counter += 1
            logger.warning(f"Payload: {payload}")
            payloads.append(payload)
            if len(payloads) == 10:
                return payloads
        
        return payloads

      
if __name__ == "__main__":


    logger.info("Testing redis connection")

    test_redis()

    logger.info("Scanner started")
    scan_config = scan_banner()
    logger.debug(scan_config)
    
    verify_key()

    while True:
        scan_config = check_scan()

        scan_id = scan_config[0]
        logger.info(f"Scan ID: {scan_id}")

        if scan_config[0] == 'none':
            time.sleep(15)
            continue
        
        scan_config = create_config(scan_category=scan_config[1], scan_type=scan_config[2], scan_speed=scan_config[3])
        
        logger.debug(scan_config)

        logger.debug("Reading the payloads")    
        payloads = read_payloads(scan_config.scan_type)

        logger.debug("Sending payloads")
        
        report = ScanReport(scan_id=scan_id)
        for payload in payloads[:-1]:
            payloadPackage = PayloadPackage(payload=payload, scan_type=scan_config.scan_type, scan_speed=scan_config.scan_speed)

            entity = payloadPackage.get_entity()
            
            payload = entity[2]
            status = payloadPackage.send_package()


            logger.warning(f"{payload} --> {status}")
            report.add(payload, status)

        logger.debug("Scan Finished")

        send_report(report.get_report(), report.get_scan_id())
        time.sleep(30)

