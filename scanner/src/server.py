from config import KEY
from requests import post
from project_logger import logger

def verify_key():
    
    logger.info(KEY)
    
    payload = {
        "key" : KEY
    }

    # resp = request(method="POST", url = f"http://host.docker.internal:5555/scanner/validate", data = payload)
    resp = post(url = f"http://localhost:5555/scanner/validate", json = payload)

    valid = resp.json()
        
    logger.warning(f"Valid: {valid['valid']}")

    if valid == "false":
        logger.error("WRONG AUTHENTICATION KEY")
        exit(0)
    
    logger.info(f"Validate request status : {resp.status_code}")

def check_scan():
    payload = {
        "key" : KEY
    }

    resp = post(url = f"http://localhost:5555/scanner/scans", json = payload)

    scan_id = resp.json()['scan_id']
    scan_category = resp.json()['scan_category']
    scan_type = resp.json()['scan_type']
    scan_speed = resp.json()['scan_speed']

    logger.debug(f"ID: {scan_id}; Category: {scan_category}; Type: {scan_type}; Speed: {scan_speed};")
    
    return (scan_id, scan_category, scan_type, scan_speed)

def send_report(report, scan_id):
    payload = {
        "scan_id" : scan_id,
        "key": KEY,
        "report": report
    }

    resp = post(url = f"http://localhost:5555/scanner/report", json = payload)

    status = resp.json()['status']

    if status == "ok":
        logger.info("Report submitted")
    else:
        logger.error("Report was not submitted")