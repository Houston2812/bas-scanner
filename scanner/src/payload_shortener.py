from project_logger import logger
from pathlib import Path
import argparse

'''
    Script to shorten the payloads from the explicit list
    Arguments:
        -i  | --input    -   input file to partse 
        -o  | --output   -   output file to store the results
        -t               -   type of the vulnerability 
'''

def parse_dirs(payloads):
    count = 0
    with open(output_file, "w") as write_file:
        for payload in payloads:
            if count == 4:
                logger.info("[+] Wrote payload to file")
                write_file.write(payload)
            count = (count + 1) % 8
            logger.debug(f"[+] Payload: {payload}")
            
if __name__ == "__main__":
    logger.info(f"[+] Parser started")
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="File that should be shrinked")
    parser.add_argument("-o", "--output", help="File to store ouput ")
    # parser.add_argument("-t", help="Type of the vulnerability listing")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    with open(input_file, "r") as file:
        logger.info(f"[+] Reading file")
        payloads = file.readlines()

        

        
