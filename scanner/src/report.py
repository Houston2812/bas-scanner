import json
from project_logger import logger

class ScanReport():
    def __init__(self, scan_id):
        self.scan_id = scan_id
        self.records = []
    
    def add(self, payload, status):
        record = {
            "payload" : payload,
            "status" : status
        }

        logger.warning(record)

        self.records.append(record)

    def get_report(self):
        report = json.dumps(self.records, indent=4)
        logger.warning(report)

        return report
    
    def get_scan_id(self):
        return self.scan_id