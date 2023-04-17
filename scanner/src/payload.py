from config import SCANNER_DIR, TARGET_URL, redisCli, KEY
from requests import Request, Session, request
from project_logger import logger
import urllib.parse
import uuid

payload_directory = f'{SCANNER_DIR}/payloads'    


class PayloadPackage():
    def __init__(self, payload, scan_type, scan_speed) -> None:
        self.__scan_type = scan_type.split('/')[-1]
        self.__scan_speed = scan_speed
        self.__payload = payload
        self.__id = str(uuid.uuid4())
        self.__url = TARGET_URL
    
    def __get_headers(self) -> dict:
        return {
                "X-Payload-Id": self.__id,
                "Content-Length": str(len(self.__payload))
               }
    
    def __get_params(self) -> dict:
        return {"payload" : self.__payload.strip()}

    def get_entity(self) -> tuple:
        return (self.__scan_type, self.__id, self.__payload)

    def __send_Get(self):
        s = Session()

        payload = self.__get_params()
        headers = self.__get_headers()

        payload_url = urllib.parse.urlencode(payload, safe=f'/%')
        logger.info(f"Payload url : {payload_url}")

        req = Request(method='GET', url=TARGET_URL, params=payload_url, headers=headers)
        prepped = req.prepare()

        prepped.url = "?".join([TARGET_URL, payload_url])

        logger.debug(f"Prepped url: {prepped.headers} --- {prepped.url} ---- {prepped.body}")

        resp = s.send(prepped)
        return resp

    def send_package(self) -> int:
        # headers = self.__get_headers()
        # params = self.__get_params()
        
        logger.info("----------")
        logger.info(f"Scan-type: {self.__scan_type}")

        result = redisCli.hmset(self.__scan_type, {self.__id : self.__payload})
        logger.debug(f"Record inserted in the redis: {self.__id}")

        r = self.__send_Get()
        data = r.json()

        response_status = data['status']
        recieved_payload = data['payload']

        logger.debug(f"Response:\n\tStatus: {response_status}\n\tReceived payload: {recieved_payload}")

        # get keys from the hash
        result = redisCli.hkeys(self.__scan_type)
        
        status = ""
        if self.__id in result:
            
            inserted_payload = redisCli.hget(self.__scan_type, self.__id)

            logger.debug(f"Inserted payload: {inserted_payload}")
            logger.debug(f"Received payload: {recieved_payload}")

            # SUPER DEBUG     
            # for index in range(len(recieved_payload) - 1):

            #     logger.warning("\n")
            #     if inserted_payload[index] == recieved_payload[index]:
            #         logger.warning("Equal")
            #     else:
            #         logger.warning("Not equal")
            #         logger.warning(f"Inserted payload element: {inserted_payload[index]}")
            #         logger.warning(f"Received payload element: {recieved_payload[index]}")
            #     logger.warning("\n")
            
            if inserted_payload[:-1].casefold() == recieved_payload.casefold():
                status = "bypassed"
                logger.info("Payload bypassed the firewall!")
            else :
                status = "blocked"
                logger.info("Payload did not bypass the firewall!")
        
        logger.info("----------")

        return status

    