import os
import redis
from dotenv import load_dotenv

load_dotenv()

SCANNER_DIR = '/scanner'
REDIS_URL = "localhost:6379"
# TARGET_URL = "http://host.docker.internal:5000/"
TARGET_URL = "http://localhost/"

KEY = os.getenv('KEY')

if 'SCAN_TYPE' in os.environ or 'SCAN_CATEGORY' in os.environ or 'SCAN_SPEED' in os.environ:
    SCAN_TYPE = os.getenv('SCAN_TYPE')
    SCAN_CATEGORY = os.getenv('SCAN_CATEGORY')
    SCAN_SPEED = os.getenv('SCAN_SPEED')
    IS_SET =  True
else:
    SCAN_CATEGORY = ''
    SCAN_TYPE = ''
    SCAN_SPEED = ''
    IS_SET = False

SCAN_CONFIG = {
    'SCAN_CATEGORY' : SCAN_CATEGORY,
    'SCAN_TYPE' : SCAN_TYPE,
    'SCAN_SPEED' : SCAN_SPEED,
}

redisCli = redis.Redis(
    host = 'localhost',
    port = 6379,
    charset = 'utf-8',
    decode_responses = True
)

def test_redis():
    try:
        connection = redisCli.ping()
    except:
        raise("Redis not initialized")
        

if __name__ == "__main__":
    load_dotenv(override=True)
