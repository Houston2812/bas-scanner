from project_logger import logger
from banner import scan_banner
from config import test_redis
from payload import PayloadPackage

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
    

    logger.debug("Reading the payloads")    
    payloads = read_payloads(scan_config.scan_type)

    logger.debug("Sending payloads")
        
    for payload in payloads[:-1]:
        payloadPackage = PayloadPackage(payload=payload, scan_type=scan_config.scan_type, scan_speed=scan_config.scan_speed)

        entity = payloadPackage.get_entity()

        status = payloadPackage.send_package()

        if status != "Received":
            logger.warning(f"Warning! Status code {status}")
    

    logger.debug("Payloads sent")


